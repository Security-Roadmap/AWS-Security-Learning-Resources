import re
import pandas as pd

def parse_level_to_category(level_str):
    """Convert level numbers to category: basic, medium, advance"""
    if not level_str:
        return "medium"
    
    # Extract numbers from level string
    numbers = re.findall(r'\d+', level_str)
    if not numbers:
        return "medium"
    
    # Get the highest level mentioned
    max_level = max(int(n) for n in numbers)
    
    if max_level <= 200:
        return "basic"
    elif max_level <= 300:
        return "medium"
    else:  # 400+
        return "advance"

def parse_workshops(content):
    """Extract workshop information from markdown content"""
    workshops = []
    
    # Find all domain sections
    domain_pattern = r'## [🔐👁️🛡️🔒🚨💻]+ Domain \d+: (.+?)\n'
    domains = re.finditer(domain_pattern, content)
    
    for domain_match in domains:
        domain_name = domain_match.group(1).strip()
        domain_start = domain_match.end()
        
        # Find next domain or end of content
        next_domain = re.search(domain_pattern, content[domain_start:])
        domain_end = domain_start + next_domain.start() if next_domain else len(content)
        domain_content = content[domain_start:domain_end]
        
        # Find all workshops in this domain (before repositories section)
        repo_section = domain_content.find('#### GitHub Repositories')
        workshop_content = domain_content[:repo_section] if repo_section != -1 else domain_content
        
        workshop_pattern = r'^\d+[a-z]?\.\s+\*\*(.+?)\*\*\n\s+- \*\*Level:\*\* (.+?)\n\s+- \*\*Duration:\*\* (.+?)\n\s+- \*\*URL:\*\* (.+?)\n\s+- \*\*Topics:\*\* (.+?)\n\s+- \*\*Best For:\*\*'
        
        for workshop_match in re.finditer(workshop_pattern, workshop_content, re.MULTILINE):
            name = workshop_match.group(1).strip()
            level = workshop_match.group(2).strip()
            duration = workshop_match.group(3).strip()
            url = workshop_match.group(4).strip()
            topics = workshop_match.group(5).strip()
            
            workshops.append({
                'Domain': domain_name,
                'Type': 'Workshop',
                'Name': name,
                'Level': parse_level_to_category(level),
                'Duration': duration,
                'URL': url,
                'Topics': topics
            })
    
    return workshops

def parse_repositories(content):
    """Extract GitHub repository information from markdown content"""
    repositories = []
    
    # Find all domain sections
    domain_pattern = r'## [🔐👁️🛡️🔒🚨💻]+ Domain \d+: (.+?)\n'
    domains = re.finditer(domain_pattern, content)
    
    for domain_match in domains:
        domain_name = domain_match.group(1).strip()
        domain_start = domain_match.end()
        
        # Find next domain or end of content
        next_domain = re.search(domain_pattern, content[domain_start:])
        domain_end = domain_start + next_domain.start() if next_domain else len(content)
        domain_content = content[domain_start:domain_end]
        
        # Find all repositories in this domain (after repositories section)
        repo_section = domain_content.find('#### GitHub Repositories')
        if repo_section == -1:
            continue
        repo_content = domain_content[repo_section:]
        
        # Match repositories with either 3 or 4 spaces indentation
        repo_pattern = r'^\d+\.\s+\*\*(.+?)\*\*\n\s+- \*\*Repository:\*\* (.+?)\n\s+- \*\*Stars:\*\*.+?\| \*\*Language:\*\*.+?\n\s+- \*\*Last Updated:\*\*.+?\n\s+- \*\*Description:\*\* (.+?)\n\s+- \*\*Topics:\*\* (.+?)\n\s+- \*\*Difficulty:\*\* (.+?)\n'
        
        for repo_match in re.finditer(repo_pattern, repo_content, re.MULTILINE):
            name = repo_match.group(1).strip()
            url = repo_match.group(2).strip()
            description = repo_match.group(3).strip()
            topics = repo_match.group(4).strip()
            difficulty = repo_match.group(5).strip().lower()
            
            # Normalize difficulty
            if difficulty == 'basic':
                level = 'basic'
            elif difficulty == 'medium':
                level = 'medium'
            else:
                level = 'advance'
            
            repositories.append({
                'Domain': domain_name,
                'Type': 'Repository',
                'Name': name,
                'Level': level,
                'Duration': '',  # Repositories don't have duration
                'URL': url,
                'Topics': topics
            })
    
    return repositories

def main():
    # Read the markdown file
    input_file = 'AWS_Security_Learning_Resources.md'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse workshops and repositories
    print("Parsing workshops...")
    workshops = parse_workshops(content)
    print(f"Found {len(workshops)} workshops")
    
    print("Parsing repositories...")
    repositories = parse_repositories(content)
    print(f"Found {len(repositories)} repositories")
    
    # Combine all resources
    all_resources = workshops + repositories
    
    # Create DataFrame
    df = pd.DataFrame(all_resources)
    
    # Reorder columns
    df = df[['Domain', 'Type', 'Name', 'Level', 'Duration', 'Topics', 'URL']]
    
    # Sort by Domain, Type, Level
    level_order = {'basic': 1, 'medium': 2, 'advance': 3}
    df['level_sort'] = df['Level'].map(level_order)
    df = df.sort_values(['Domain', 'Type', 'level_sort'])
    df = df.drop('level_sort', axis=1)
    
    # Export to CSV
    csv_file = 'AWS_Security_Resources_Table.csv'
    df.to_csv(csv_file, index=False, encoding='utf-8')
    print(f"\nExported to {csv_file}")
    
    # Export to Excel with better formatting
    excel_file = 'AWS_Security_Resources_Table.xlsx'
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='All Resources', index=False)
        
        # Get the worksheet
        worksheet = writer.sheets['All Resources']
        
        # Adjust column widths
        worksheet.column_dimensions['A'].width = 35  # Domain
        worksheet.column_dimensions['B'].width = 12  # Type
        worksheet.column_dimensions['C'].width = 60  # Name
        worksheet.column_dimensions['D'].width = 10  # Level
        worksheet.column_dimensions['E'].width = 12  # Duration
        worksheet.column_dimensions['F'].width = 70  # Topics
        worksheet.column_dimensions['G'].width = 80  # URL
        
    print(f"Exported to {excel_file}")
    
    # Print summary statistics
    print("\n=== Summary Statistics ===")
    print(f"Total Resources: {len(df)}")
    print(f"\nBy Type:")
    print(df['Type'].value_counts())
    print(f"\nBy Level:")
    print(df['Level'].value_counts())
    print(f"\nBy Domain:")
    print(df['Domain'].value_counts())

if __name__ == "__main__":
    main()
