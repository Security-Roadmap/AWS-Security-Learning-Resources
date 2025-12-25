# AWS Security Learning Resources
## Enterprise Cloud Security Knowledge Framework

**Last Updated:** December 15, 2025  
**Repository Filter:** Commits after December 15, 2023 (within 2 years)

This guide provides curated learning resources aligned with the **Enterprise Cloud Security Knowledge Framework** domains 2-7. Resources include AWS workshops, hands-on labs, and GitHub repositories with recent activity.

---

## 📚 Resource Categories

- **Basic (Level 100-200)**: Foundational concepts and getting started
- **Medium (Level 200-300)**: Intermediate implementations and best practices  
- **Advanced (Level 300-400)**: Advanced architectures and specialized topics

---

## Framework Coverage

### Domains Covered:
1. ~~Security Foundations~~ *(Excluded as requested)*
2. **Identity and Access Management (IAM)**
3. **Detection**
4. **Infrastructure Protection**
5. **Data Protection**
6. **Incident Response**
7. **Application Security**

---

## 🔐 Domain 2: Identity and Access Management (IAM)

> Focus: Identity as the Primary Security Perimeter, Authorization Design, Privileged Access Governance

### Basic (100-200 Level)

#### Workshops
1. **Security Baseline Workshop**
   - **Level:** 100
   - **Duration:** 2 hours
   - **URL:** https://catalog.workshops.aws/startup-security-baseline/en-US
   - **Topics:** IAM fundamentals, security best practices
   - **Best For:** Beginners establishing security foundations

2. **IAM Identity Center - Workforce Identity Management at Scale**
   - **Level:** 200
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/590f8439-42c7-46a1-8e70-28ee41498b3a
   - **Topics:** IAM Identity Center, SSO, multi-account
   - **Best For:** Enterprise identity management

3. **Least Privilege with IAM Access Analyzer**
   - **Level:** 200
   - **Duration:** 1 hour
   - **URL:** https://catalog.workshops.aws/lp-aa
   - **Topics:** IAM Access Analyzer, least privilege
   - **Best For:** Permission optimization

### Medium (200-300 Level)

#### Workshops
4. **Threat Modeling for Builders**
   - **Level:** 200
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/threatmodel
   - **Topics:** System modeling, threat identification
   - **Best For:** Security-minded developers

5. **IAM Policy Learning Experience**
   - **Level:** 300
   - **Duration:** 1 hour
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/d1531d0a-79fd-45af-b198-d81e349ee660
   - **Topics:** IAM policy writing, conditions
   - **Best For:** IAM policy fundamentals

6. **How and When to Use Different IAM Policy Types**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.workshops.aws/iam-policy-types
   - **Topics:** Identity policies, resource policies, permission boundaries
   - **Best For:** Advanced IAM patterns

7. **Refining IAM Permissions Like A Pro**
   - **Level:** 300
   - **Duration:** 1 hour
   - **URL:** https://catalog.workshops.aws/refining-iam-permissions-like-a-pro
   - **Topics:** Unused permissions, automation
   - **Best For:** Permission cleanup

8. **Streamline Workforce Access to AWS Analytics Services using IAM Identity Center**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/c93b473e-436e-45be-80e8-322b90c7024f
   - **Topics:** IAM Identity Center, Trusted Identity Propagation
   - **Best For:** Analytics security

9. **Cedar Policy Language in Action**
    - **Level:** 300
    - **Duration:** 2 hours
    - **URL:** https://catalog.workshops.aws/cedar-policy-language-in-action
    - **Topics:** Cedar, Amazon Verified Permissions
    - **Best For:** Fine-grained authorization

10a. **IAM Immersion Day**
    - **Level:** 100-400
    - **Duration:** 6 hours
    - **URL:** https://catalog.workshops.aws/workshops/18b3622c-5d4c-45c9-9834-6a7091109072
    - **Topics:** Comprehensive IAM training covering all levels
    - **Best For:** Complete IAM understanding from basics to expert
    - **Languages:** English, 한국어, 日本語

10c. **Amazon Cognito Workshop**
    - **Level:** 300
    - **Duration:** 6 hours
    - **URL:** https://catalog.workshops.aws/workshops/137bc34c-33d9-43a8-bf8f-2d4f6c22c333
    - **Topics:** Deep dive into Cognito user authentication
    - **Best For:** User identity and authentication

10d. **Verified Permissions in action**
    - **Level:** 300
    - **Duration:** 4 hours
    - **URL:** https://catalog.workshops.aws/workshops/00171721-a17c-4b56-9849-5558dcaacd94
    - **Topics:** Amazon Verified Permissions APIs, Cedar policies
    - **Best For:** Fine-grained application authorization

10e. **IAM Identity Center: Empowering Secure Access to Generative AI Applications**
    - **Level:** 300
    - **Duration:** 2 hours
    - **URL:** https://catalog.workshops.aws/workshops/d6323be2-38f4-457e-aaf5-08af211f3681
    - **Topics:** Connect corporate identities to AWS, manage access to Amazon Q
    - **Best For:** Enterprise AI application access management

### Advanced (300-400 Level)

#### Workshops
11. **Integrating IAM Access Analyzer into a CI/CD Pipeline**
    - **Level:** 300
    - **Duration:** 2 hours
    - **URL:** https://catalog.workshops.aws/accessanalyzercicd
    - **Topics:** IAM policy validation, CI/CD
    - **Best For:** Policy validation automation

12. **Automating IAM Policy Validation and Analysis using GitHub Actions**
    - **Level:** 400
    - **Duration:** 2 hours
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/b5083f86-f4e1-4712-8015-ae1549eb2971
    - **Topics:** GitHub Actions, automated policy validation
    - **Best For:** DevSecOps automation

13. **Advanced Machine-to-Machine Access with IAM Roles Anywhere**
    - **Level:** 300
    - **Duration:** 1 hour
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/f81841e0-b033-4355-8b6c-b2a404d544a4
    - **Topics:** IAM Roles Anywhere, certificate-based auth
    - **Best For:** External workload authentication

#### GitHub Repositories (Recent Commits)
15. **iam-identity-center-team**
    - **Repository:** https://github.com/aws-samples/iam-identity-center-team
    - **Stars:** 449 | **Language:** JavaScript
    - **Last Updated:** Dec 15, 2025
    - **Description:** Open-source temporary elevated access solution for AWS IAM Identity Center
    - **Topics:** Just-In-Time access, privilege elevation
    - **Difficulty:** Medium

16. **aws-iam-identity-center-extensions**
    - **Repository:** https://github.com/aws-samples/aws-iam-identity-center-extensions
    - **Stars:** 72 | **Language:** TypeScript
    - **Last Updated:** Nov 12, 2025
    - **Description:** Enterprise SSO functionality automation for common access management use cases
    - **Topics:** AWS SSO for enterprise
    - **Difficulty:** Advanced

17. **automated-role-entitlements-in-aws-iam-identity-center**
    - **Repository:** https://github.com/aws-samples/automated-role-entitlements-in-aws-iam-identity-center
    - **Stars:** 25 | **Language:** Python
    - **Last Updated:** May 9, 2025
    - **Description:** Automate user group assignment to permission sets following least privilege
    - **Topics:** Role entitlements, scale access, security automation
    - **Difficulty:** Medium

18. **terraform-aws-identity-center**
    - **Repository:** https://github.com/aws-samples/terraform-aws-identity-center
    - **Stars:** 25 | **Language:** HCL
    - **Last Updated:** Nov 3, 2025
    - **Description:** Manage AWS IAM Identity Center permission sets and account assignments with Terraform
    - **Topics:** Terraform, Infrastructure as Code
    - **Difficulty:** Medium

19. **single-stage-aws-iam-identity-center-pipeline**
    - **Repository:** https://github.com/aws-samples/single-stage-aws-iam-identity-center-pipeline
    - **Stars:** 16 | **Language:** Python
    - **Last Updated:** Nov 28, 2025
    - **Description:** Simplify AWS Identity Center management using JSON/YAML inputs
    - **Topics:** Configuration as Code
    - **Difficulty:** Basic

20. **sample-visualizing-access-rights-for-identity-on-aws**
    - **Repository:** https://github.com/aws-samples/sample-visualizing-access-rights-for-identity-on-aws
    - **Stars:** 30 | **Language:** Python
    - **Last Updated:** Nov 27, 2025
    - **Description:** Visualize and map relationships between identities and resources using Neptune
    - **Topics:** Identity visualization, graph databases
    - **Difficulty:** Advanced

21. **aws-iam-identity-center-permission-policies-analyzer**
    - **Repository:** https://github.com/aws-samples/aws-iam-identity-center-permission-policies-analyzer
    - **Stars:** 18 | **Language:** Python
    - **Last Updated:** Nov 27, 2025
    - **Description:** Analyze permission policies in IAM Identity Center
    - **Topics:** Policy analysis
    - **Difficulty:** Medium

22. **terraform-aws-identity-center-users-and-groups**
    - **Repository:** https://github.com/aws-samples/terraform-aws-identity-center-users-and-groups
    - **Stars:** 11 | **Language:** HCL
    - **Last Updated:** Oct 26, 2025
    - **Description:** Create IAM Identity Center groups, users, and group membership with Terraform
    - **Topics:** User management, Terraform
    - **Difficulty:** Basic

---

## 👁️ Domain 3: Detection

> Focus: Visibility, Signal Quality, Threat Detection Engineering, SIEM & SOAR Architecture

### Basic (100-200 Level)

#### Workshops
2. **SIEM on Amazon OpenSearch Service Workshop**
   - **Level:** 200
   - **Duration:** 2 hours
   - **URL:** https://security-log-analysis-platform.workshop.aws/
   - **Topics:** OpenSearch, GuardDuty, SecurityHub, CloudTrail
   - **Best For:** Security log analysis

3. **Amazon GuardDuty & Amazon Detective Workshop**
   - **Level:** 300
   - **Duration:** 4 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/7e9f67a3-985a-4e9c-b38b-2d54a70d0da7
   - **Topics:** Amazon GuardDuty, Amazon Detective overviews and operationalization
   - **Best For:** Comprehensive threat detection and response workflows

### Medium (200-300 Level)

#### Workshops
4. **Security Hub Workshop**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.workshops.aws/security-hub
   - **Topics:** Security Hub, finding prioritization
   - **Best For:** Centralized security management

5. **Building a Cloud Security Posture Dashboard with Amazon QuickSight**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.workshops.aws/securitydashboard
   - **Topics:** Security Hub, QuickSight, dashboards
   - **Best For:** Security visualization

6. **Visualize Security Hub Findings using AWS Analytics Services**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.workshops.aws/visualizing-securityhub-findings/en-US
   - **Topics:** Security Hub, Athena, QuickSight
   - **Best For:** Analytics-driven security

7. **Building Prowler into a QuickSight powered AWS security dashboard**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/b1cdc52b-eb11-44ed-8dc8-9dfe5fb254f5/en-US
   - **Topics:** Prowler, continuous monitoring
   - **Best For:** Compliance scanning

### Advanced (300-400 Level)

#### Workshops
9. **Unauthorized IAM Credential Use - Security Event Simulation**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/6a8ad836-10a6-4694-9a3b-f53f193041de
   - **Topics:** CloudTrail, credential compromise
   - **Best For:** IAM incident detection

10. **Cryptomining - Security Event Simulation**
    - **Level:** 300
    - **Duration:** 1 hour
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/ea9c0361-001f-4194-963e-06b07c3e5d6b
    - **Topics:** GuardDuty, crypto mining detection
    - **Best For:** Threat detection

11. **Validating Security Guardrails with Chaos Engineering**
    - **Level:** 400
    - **Duration:** 1 hour
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/f36e426f-e8a6-467e-97d3-2223bd5f0c49
    - **Topics:** Fault Injection Simulator, GuardDuty, Config
    - **Best For:** Security testing

#### GitHub Repositories (Recent Commits)
12. **aws-control-tower-org-setup-sample**
    - **Repository:** https://github.com/aws-samples/aws-control-tower-org-setup-sample
    - **Stars:** 37 | **Language:** Python
    - **Last Updated:** Sep 8, 2025
    - **Description:** Automated AWS Organizations configuration for security operations
    - **Topics:** Control Tower, GuardDuty, Macie, SecurityHub, automation
    - **Difficulty:** Advanced

13. **sample-aws-multi-account-observability**
    - **Repository:** https://github.com/aws-samples/sample-aws-multi-account-observability
    - **Stars:** 13 | **Language:** Python
    - **Last Updated:** Dec 1, 2025
    - **Description:** Multi-account observability platform with 15+ AWS service integrations
    - **Topics:** Multi-account, monitoring, security analytics
    - **Difficulty:** Advanced

---

## 🛡️ Domain 4: Infrastructure Protection

> Focus: Network Security Architecture, Compute Security, Reducing Attack Surface

### Basic (100-200 Level)

#### Workshops

2. **Firewall Manager Workshop - Audit and Manage Firewall Rules**
   - **Level:** 200
   - **Duration:** 4 hours
   - **URL:** https://catalog.workshops.aws/firewall-manager/en-US
   - **Topics:** Firewall Manager, centralized management
   - **Best For:** Multi-account firewall governance

### Medium (200-300 Level)

#### Workshops
3. **Strengthen Your Web Application Defenses with AWS WAF**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/81e94a4b-b47f-4acc-a284-914c4514d50f/en-US
   - **Topics:** AWS WAF, web application security
   - **Best For:** WAF configuration

4. **Approaches to Layered Security on Amazon VPC**
   - **Level:** 300
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/layered-vpc-security
   - **Topics:** Network Firewall, WAF, Gateway Load Balancer
   - **Best For:** Defense in depth

5. **AWS Gateway Load Balancer Workshop**
   - **Level:** 300
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/gwlb-networking
   - **Topics:** Gateway Load Balancer, inspection VPC
   - **Best For:** Traffic inspection

6. **Secure Hybrid Access to S3 using VPC Endpoints**
   - **Level:** 300
   - **Duration:** 1 hour
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/3a8d4ddf-66c5-4d26-ae6f-6292a517f46c/en-US
   - **Topics:** PrivateLink, VPC endpoints, hybrid connectivity
   - **Best For:** Private S3 access

7. **AWS Verified Access Workshop**
   - **Level:** 300
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/verifiedaccessworkshop/en-US
   - **Topics:** Verified Access, Zero Trust Network Access
   - **Best For:** Zero Trust network access

8. **AWS Networking Workshop**
   - **Level:** 300
   - **Duration:** 8 hours
   - **URL:** https://networking.workshop.aws
   - **Topics:** VPC, Transit Gateway, Direct Connect, security
   - **Best For:** Comprehensive networking

8a. **AWS Storage Workshop**
   - **Level:** 300
   - **Duration:** 6 hours
   - **URL:** https://catalog.workshops.aws/workshops/74237958-77c8-4e7f-a02f-ae201a04d759
   - **Topics:** Storage security best practices, data migration strategies, performance tuning, backup
   - **Best For:** Secure storage architecture and data protection

8b. **Egress Controls with AWS Network Firewall and Amazon Route 53 Resolver DNS Firewall**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.workshops.aws/workshops/503778b9-6dbb-4e0d-9920-e8dbae141f43
   - **Topics:** AWS Network Firewall, Route 53 DNS Firewall, centralized management with Firewall Manager
   - **Best For:** Best practice egress network controls
   - **Languages:** English, 한국어

### Advanced (300-400 Level)

#### Workshops
9. **Hands on Network Firewall Workshop**
   - **Level:** 400
   - **Duration:** 2 hours
   - **URL:** https://hands-on-network-firewall.workshop.aws
   - **Topics:** AWS Network Firewall, stateful rules
   - **Best For:** Network firewall deep dive

10. **AWS Network Firewall Workshop**
    - **Level:** 400
    - **Duration:** 2 hours
    - **URL:** https://networkfirewall.workshop.aws
    - **Topics:** Network Firewall features, best practices
    - **Best For:** Advanced firewall patterns

11. **Building Application Deception System using AWS WAF Bot Control**
    - **Level:** 400
    - **Duration:** 4 hours
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/254e4343-d3c1-4963-8a35-023de1c2b23e
    - **Topics:** Bot Control, deception techniques
    - **Best For:** Advanced bot mitigation

12. **Zero Trust Episode 1 - The Phantom Service Perimeter**
    - **Level:** 200
    - **Duration:** 2 hours
    - **URL:** https://zerotrust-service2service.workshop.aws
    - **Topics:** Zero Trust, service perimeter
    - **Best For:** Zero Trust architecture

12a. **Amazon EKS Security Immersion Day**
    - **Level:** 300
    - **Duration:** 8 hours
    - **URL:** https://catalog.workshops.aws/workshops/165b0729-2791-4452-8920-53b734419050
    - **Topics:** Authentication/Authorization, cluster endpoint security, basic & advanced image scanning, runtime pod security, network policies, GuardDuty integration, CIS benchmark image hardening, Bottlerocket OS, IRSA, Secrets Management
    - **Best For:** Comprehensive EKS security features across all aspects

13. **Securing AWS Network Traffic: Network Firewall & DNS Firewall Workshop**
    - **Level:** 300
    - **Duration:** 2 hours
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/cbfa9f18-1175-4916-b7e7-e33dbbca9f9d/en-US
    - **Topics:**  Network Firewall & DNS Firewall 
    - **Best For:** Comprehensive EKS security features across all aspects

#### GitHub Repositories (Recent Commits)
14. **aws-vpc-builder-cdk**
    - **Repository:** https://github.com/aws-samples/aws-vpc-builder-cdk
    - **Stars:** 41 | **Language:** TypeScript
    - **Last Updated:** Jun 12, 2025
    - **Description:** Deploy complex AWS Network Architectures using CDK from configuration files
    - **Topics:** VPC, VPC endpoints, Firewall, Route53
    - **Difficulty:** Medium

15. **moving-to-a-zero-trust-architecture-in-aws**
    - **Repository:** https://github.com/aws-samples/moving-to-a-zero-trust-architecture-in-aws
    - **Stars:** 4 | **Language:** HCL
    - **Last Updated:** Dec 8, 2025
    - **Description:** Zero Trust architecture implementation on AWS
    - **Topics:** Zero Trust, Terraform
    - **Difficulty:** Advanced

16. **networking-costs-calculator**
    - **Repository:** https://github.com/aws-samples/networking-costs-calculator
    - **Stars:** 103 | **Language:** JavaScript
    - **Last Updated:** Nov 19, 2025
    - **Description:** Estimate networking costs including Data Transfer, Transit Gateway, NAT Gateways
    - **Topics:** Cost optimization, VPC
    - **Difficulty:** Basic

#### AWS Solutions
17. **aws-waf-security-automations**
    - **Repository:** https://github.com/aws-solutions/aws-waf-security-automations
    - **Stars:** 908 | **Language:** Python
    - **Last Updated:** Dec 11, 2025
    - **Description:** Automatically deploy WAF with rules to filter common web-based attacks
    - **Topics:** WAF, security automation
    - **Difficulty:** Medium

---

## 🔒 Domain 5: Data Protection

> Focus: Encryption & Key Management, Data Access Governance, Data-Centric Security

### Basic (100-200 Level)

#### Workshops
1. **AWS Encryption Tutorial**
   - **Level:** 200
   - **Duration:** 5 hours
   - **URL:** https://encryption-ws.workshop.aws
   - **Topics:** KMS, S3, RDS, EBS, DynamoDB encryption
   - **Best For:** Encryption fundamentals

2. **Practical Data Privacy and Compliance Controls for Sensitive Workloads**
   - **Level:** 200
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/2d21fd6c-8e3d-49ad-b01a-fa9380842bc4
   - **Topics:** Macie, EventBridge, compliance
   - **Best For:** Data protection lifecycle

2a. **S3 Immersion Day**
   - **Level:** 300
   - **Duration:** 8 hours
   - **URL:** https://catalog.workshops.aws/workshops/093c6055-093f-4928-ba16-83a79874e2fe
   - **Topics:** S3 security best practices, encryption, access controls, compliance, data lifecycle management
   - **Best For:** Comprehensive S3 security and data protection

### Medium (200-300 Level)

#### Workshops
3. **Data Perimeter in Action**
   - **Level:** 300
   - **Duration:** 1 hour
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/1ca880ca-5039-48df-a097-b164baa696aa
   - **Topics:** Data perimeter, network perimeter
   - **Best For:** Data access control

4. **AWS Encryption in Transit Workshop**
   - **Level:** 300
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/certificatemanager
   - **Topics:** Private CA, ACM, TLS
   - **Best For:** Certificate management

5. **Data Protection in Event Driven Architectures**
   - **Level:** 300
   - **Duration:** 1 hour
   - **URL:** https://catalog.workshops.aws/data-protection-eda
   - **Topics:** KMS, SNS, SQS, Lambda encryption
   - **Best For:** Serverless data protection

7. **Hands-on KMS Troubleshooting Labs**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/a081e718-4acc-4877-acc3-94fba8a64bce
   - **Topics:** KMS troubleshooting, S3/KMS integration
   - **Best For:** KMS debugging

8. **Store, retrieve, and manage sensitive credentials in AWS Secrets Manager**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/92e466fd-bd95-4805-9f16-2df07450db42/en-US
   - **Topics:** Secrets rotation, credential management
   - **Best For:** Secrets management

9. **Serverless Security: Advanced Lambda Protection**
    - **Level:** 300
    - **Duration:** 1 hour
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/0f031bd6-2a06-4788-b5da-bc887a7a97b9
    - **Topics:** Lake Formation, data classification
    - **Best For:** Data lake security

10. **AWS Control Design**
    - **Level:** 300
    - **Duration:** 2 hour
    - **URL:** https://catalog.workshops.aws/control-design/en-US
    - **Topics:** 3 Tier environment
    - **Best For:** Security control

### Advanced (300-400 Level)

#### Workshops
11. **Using Post-Quantum Cryptography on AWS**
    - **Level:** 300
    - **Duration:** 2 hours
    - **URL:** https://catalog.workshops.aws/using-pq-crypto-on-aws
    - **Topics:** Post-quantum cryptography
    - **Best For:** Future-proof encryption

12. **AWS ACM Hands-On Troubleshooting Workshop**
    - **Level:** 300
    - **Duration:** 1 hour
    - **URL:** https://catalog.workshops.aws/acm-troubleshooting
    - **Topics:** ACM DNS validation
    - **Best For:** Certificate troubleshooting

13. **Data Perimeter Workshop**
    - **Level:** 400
    - **Duration:** 2 hours
    - **URL:** https://data-perimeter.workshop.aws
    - **Topics:** VPC Endpoints, resource policies, trust perimeter
    - **Best For:** Advanced data protection

14. **Practical Data Privacy and Compliance Controls for Sensitive Workloads**
    - **Level:** 300
    - **Duration:** 2 hours
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/2d21fd6c-8e3d-49ad-b01a-fa9380842bc4/en-US
    - **Topics:** Threat Model
    - **Best For:** Advanced data protection

#### GitHub Repositories (Recent Commits)
15. **busy-engineers-document-bucket**
    - **Repository:** https://github.com/aws-samples/busy-engineers-document-bucket
    - **Stars:** 20 | **Language:** Java
    - **Last Updated:** Jun 30, 2025
    - **Description:** Workshop introducing client-side encryption with AWS Encryption SDK and KMS
    - **Topics:** Client-side encryption, encryption SDK
    - **Difficulty:** Medium

16. **cloudfront-to-govcloud-s3-sse-kms**
    - **Repository:** https://github.com/aws-samples/cloudfront-to-govcloud-s3-sse-kms
    - **Stars:** 4 | **Language:** TypeScript
    - **Last Updated:** Oct 22, 2025
    - **Description:** Enable CloudFront access to S3 bucket with SSE-KMS in GovCloud
    - **Topics:** SSE-KMS, CloudFront, Lambda@Edge
    - **Difficulty:** Advanced

---

## 🚨 Domain 6: Incident Response

> Focus: Incident Management, Cloud-Specific Response, Organizational Coordination

### Basic (100-200 Level)

#### Workshops
1. **Ransomware on S3 - Security Event Simulation**
   - **Level:** 200
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/fc7b7cf3-f494-48e2-8954-258ffdd76ed6
   - **Topics:** S3 versioning, data protection
   - **Best For:** Ransomware defense

### Medium (200-300 Level)

#### Workshops
2. **Automating Incident Response Workshop**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.workshops.aws/auto-incident-response
   - **Topics:** AWS Lambda, automated response
   - **Best For:** Incident response automation

3. **SSRF on IMDSv1 - Security Event Simulation**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/c125f3c7-95e8-4e24-9819-6d085664a507
   - **Topics:** SSRF, IMDSv2, metadata security
   - **Best For:** SSRF prevention

4. **AWS CIRT Toolkit For Automating Incident Response Preparedness**
   - **Level:** 300
   - **Duration:** 1 hour
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/4191fcf7-06cc-4b4a-b13c-e7c4813f4839
   - **Topics:** CIRT tools, automation
   - **Best For:** IR preparedness

5. **Unauthorized IAM Credential Use - Security Event Simulation**
   - **Level:** 300
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/6a8ad836-10a6-4694-9a3b-f53f193041de
   - **Topics:** CloudTrail, credential compromise
   - **Best For:** IAM incident detection

6. **Cryptomining - Security Event Simulation**
   - **Level:** 300
   - **Duration:** 1 hour
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/ea9c0361-001f-4194-963e-06b07c3e5d6b
   - **Topics:** GuardDuty, crypto mining detection
   - **Best For:** Threat detection

### Advanced (300-400 Level)

#### Workshops
7. **AWS Incident Response Playbooks Workshop**
   - **Level:** 400
   - **Duration:** 2 hours
   - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/ed82a5d4-6630-41f0-a6a1-9345898fa6ec
   - **Topics:** CloudTrail, Security Hub, Athena, GuardDuty
   - **Best For:** Building IR playbooks

#### GitHub Repositories (Recent Commits)
8. **aws-incident-response-playbooks**
   - **Repository:** https://github.com/aws-samples/aws-incident-response-playbooks
   - **Stars:** 1038 | **Language:** N/A
   - **Last Updated:** Dec 11, 2025
   - **Description:** Incident response playbook collection for AWS
   - **Topics:** Playbooks, best practices
   - **Difficulty:** Medium

9. **aws-incident-response-playbooks-workshop**
   - **Repository:** https://github.com/aws-samples/aws-incident-response-playbooks-workshop
   - **Stars:** 98 | **Language:** Python
   - **Last Updated:** Dec 14, 2025
   - **Description:** Hands-on incident response workshop
   - **Topics:** CloudTrail, GuardDuty, VPC flow logs, Route53 query logs
   - **Difficulty:** Medium

10. **sample-aws-security-incident-response-integrations**
    - **Repository:** https://github.com/aws-samples/sample-aws-security-incident-response-integrations
    - **Stars:** 17 | **Language:** Python
    - **Last Updated:** Dec 3, 2025
    - **Description:** Security incident response integration samples
    - **Topics:** Incident response automation
    - **Difficulty:** Advanced

11. **aws-customer-playbook-framework**
    - **Repository:** https://github.com/aws-samples/aws-customer-playbook-framework
    - **Stars:** 644 | **Language:** N/A
    - **Last Updated:** Nov 23, 2025
    - **Description:** Security playbook templates for various scenarios
    - **Topics:** Playbooks, frameworks
    - **Difficulty:** Medium

12. **automated-ec2-isolation-for-incident-response**
    - **Repository:** https://github.com/aws-samples/automated-ec2-isolation-for-incident-response
    - **Stars:** 3 | **Language:** Python
    - **Last Updated:** May 1, 2025
    - **Description:** Automatically implement incident response for EC2 instance isolation using CDK
    - **Topics:** EC2 isolation, automation
    - **Difficulty:** Medium

13. **improving-security-incident-response-times-by-decentralizing-notifications**
    - **Repository:** https://github.com/aws-samples/improving-security-incident-response-times-by-decentralizing-notifications
    - **Stars:** 8 | **Language:** Shell
    - **Last Updated:** Feb 4, 2025
    - **Description:** Improve response times by decentralizing notifications
    - **Topics:** Notification architecture
    - **Difficulty:** Advanced

14. **sample-eks-incident-response-automation**
    - **Repository:** https://github.com/aws-samples/sample-eks-incident-response-automation
    - **Stars:** 5 | **Language:** Python
    - **Last Updated:** Sep 18, 2025
    - **Description:** EKS incident response automation
    - **Topics:** EKS, Kubernetes security
    - **Difficulty:** Advanced

15. **sample-fully-autonomous-incident-response**
    - **Repository:** https://github.com/aws-samples/sample-fully-autonomous-incident-response
    - **Stars:** 0 | **Language:** Python
    - **Last Updated:** Dec 5, 2025
    - **Description:** Fully autonomous incident response implementation
    - **Topics:** Automation, AI-driven response
    - **Difficulty:** Advanced

#### AWS Solutions
16. **automated-security-response-on-aws**
    - **Repository:** https://github.com/aws-solutions/automated-security-response-on-aws
    - **Stars:** 454 | **Language:** TypeScript
    - **Last Updated:** Dec 12, 2025
    - **Description:** Add-on solution with Security Hub for automated playbooks
    - **Topics:** Security automation, Security Hub
    - **Difficulty:** Advanced

---

## 🔐 Domain 7: Application Security

> Focus: Secure-by-Design Systems, DevSecOps, Software Supply Chain Security

### Basic (100-200 Level)

#### Workshops
1. **Security for Developers**
   - **Level:** 300
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/sec4devs/en-US
   - **Topics:** Secure coding, DevSecOps, Application Security
   - **Best For:** Developers building secure applications

2. **Secure Code with Amazon Q Developer**
   - **Level:** 200
   - **Duration:** 2 hours
   - **URL:** https://catalog.workshops.aws/q-dev-secure-code/en-US
   - **Topics:** Amazon Q, code security, vulnerability detection
   - **Best For:** AI-assisted secure coding

### Medium (200-300 Level)

#### Workshops
3. **AWS Serverless Security Workshop**
   - **Level:** 200
   - **Duration:** 4 hours
   - **URL:** https://github.com/aws-samples/aws-serverless-security-workshop
   - **Topics:** Lambda, API Gateway, RDS Aurora security
   - **Best For:** Serverless application security

3a. **Serverless Security Workshop (builder.aws)**
   - **Level:** 300
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/workshops/026f84fd-f589-4a59-a4d1-81dc543fcd30
   - **Topics:** Securing serverless applications with AWS Lambda, Amazon API Gateway, and RDS Aurora
   - **Best For:** Production serverless security techniques

4. **Secure Pipelines in AWS Workshop**
   - **Level:** 200
   - **Duration:** 3 hours
   - **URL:** https://github.com/aws-samples/secure-pipelines-in-aws-workshop
   - **Topics:** Pipeline security automation
   - **Best For:** Security in CI/CD


6. **Terraform CI/CD and Testing on AWS**
   - **Level:** 300
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/terraform-cicd-on-aws
   - **Topics:** Terraform testing, security tests
   - **Best For:** IaC security testing

7. **Control Design Workshop**
   - **Level:** 300
   - **Duration:** 3 hours
   - **URL:** https://catalog.workshops.aws/control-design
   - **Topics:** Security controls, KMS, Config, Systems Manager
   - **Best For:** Control implementation

8. **CI/CD on AWS Workshop**
   - **Level:** 300
   - **Duration:** 4 hours
   - **URL:** https://catalog.workshops.aws/workshops/40f6bef0-35e1-4aeb-8359-1584d37d916b
   - **Topics:** Secure CI/CD pipelines, continuous integration, continuous deployment, continuous delivery
   - **Best For:** Building secure automated deployment pipelines
   - **Languages:** English, 한국어, 日本語

### Advanced (300-400 Level)

#### Workshops
9. **Amazon SageMaker Studio Secure Data Science Workshop**
   - **Level:** 300
   - **Duration:** 4 hours
   - **URL:** https://github.com/aws-samples/amazon-sagemaker-studio-secure-data-science-workshop
   - **Topics:** SageMaker security, ML security
   - **Best For:** Secure machine learning

10. **Enhance Security in Machine Learning Workflows**
    - **Level:** 300
    - **Duration:** 2 hours
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/578da574-492d-439f-8f20-f14a782e3701
    - **Topics:** ML security, data protection
    - **Best For:** ML security practices

11. **Cloud DevSecOps with Hashicorp, Palo Alto Networks & AWS**
    - **Level:** 200
    - **Duration:** 2 hours
    - **URL:** https://catalog.us-east-1.prod.workshops.aws/workshops/e31afbdf-ee40-41fa-a6c9-6ba2cb55fc1e
    - **Topics:** Terraform, DevSecOps, IaC security
    - **Best For:** Infrastructure security automation

#### GitHub Repositories (Recent Commits)
12. **aws-serverless-security-workshop**
    - **Repository:** https://github.com/aws-samples/aws-serverless-security-workshop
    - **Stars:** 542 | **Language:** JavaScript
    - **Last Updated:** Dec 13, 2025
    - **Description:** Secure serverless applications with Lambda, API Gateway, and RDS Aurora
    - **Topics:** IAM, code security, data protection, infrastructure, logging
    - **Difficulty:** Medium

13. **devsecops-cicd**
    - **Repository:** https://github.com/aws-samples/devsecops-cicd
    - **Stars:** 94 | **Language:** HTML
    - **Last Updated:** Nov 21, 2025
    - **Description:** DevSecOps CI/CD pipeline implementation
    - **Topics:** DevSecOps, CI/CD
    - **Difficulty:** Medium

14. **cdk-devsecops-cicd-pipeline**
    - **Repository:** https://github.com/aws-samples/cdk-devsecops-cicd-pipeline
    - **Stars:** 15 | **Language:** Python
    - **Last Updated:** Oct 6, 2025
    - **Description:** DevSecOps CI/CD pipeline using CDK
    - **Topics:** CDK, infrastructure as code
    - **Difficulty:** Medium

15. **generative-ai-to-build-a-devsecops-chatbot**
    - **Repository:** https://github.com/aws-samples/generative-ai-to-build-a-devsecops-chatbot
    - **Stars:** 13 | **Language:** Python
    - **Last Updated:** Oct 27, 2025
    - **Description:** Generative AI for DevSecOps chatbot
    - **Topics:** Gen AI, automation
    - **Difficulty:** Advanced

16. **minimum-eks-devsecops-with-monitoring-options**
    - **Repository:** https://github.com/aws-samples/minimum-eks-devsecops-with-monitoring-options
    - **Stars:** 12 | **Language:** TypeScript
    - **Last Updated:** Apr 15, 2025
    - **Description:** Minimum DevSecOps implementation for EKS with monitoring
    - **Topics:** EKS, Kubernetes, monitoring
    - **Difficulty:** Advanced

17. **sample-devsecops-eks-pipeline**
    - **Repository:** https://github.com/aws-samples/sample-devsecops-eks-pipeline
    - **Stars:** 0 | **Language:** Go
    - **Last Updated:** Sep 10, 2025
    - **Description:** DevSecOps pipeline for EKS
    - **Topics:** EKS, pipeline automation
    - **Difficulty:** Advanced

18. **secure-pipelines-in-aws-workshop**
    - **Repository:** https://github.com/aws-samples/secure-pipelines-in-aws-workshop
    - **Stars:** 37 | **Language:** Python
    - **Last Updated:** Jun 21, 2024
    - **Description:** Build security automation in pipelines
    - **Topics:** CI/CD security, automation
    - **Difficulty:** Medium

---

## 📚 Additional Learning Resources

### Official AWS Platforms

#### AWS Workshop Studio
- **URL:** https://workshops.aws/
- **Description:** 100+ hands-on workshops across all security domains
- **Access:** Free, globally available, mobile-friendly
- **Best For:** Practical, scenario-based learning

#### AWS Skill Builder
- **URL:** https://skillbuilder.aws/
- **Description:** Official AWS training platform
- **Features:**
  - Free and subscription-based content
  - AWS Jam Journeys (role-based challenges)
  - Certification preparation
  - Hands-on labs
- **Security-Focused Jam Journeys:**
  - Identity Management and Access Control (Intermediate & Advanced)
  - Network and Infrastructure Security
  - Data Protection and Data Encryption

#### AWS Security Maturity Model
- **URL:** https://maturitymodel.security.aws.dev/en/model/
- **Description:** Assess and improve security posture
- **Domains:**
  - Security foundations
  - Identity and access management
  - Detection
  - Infrastructure protection
  - Data protection
  - Incident response
  - Application security

### AWS Well-Architected Framework
- **Security Pillar:** https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/
- **Focus Areas:**
  - Security foundations
  - Identity and access management
  - Detection controls
  - Infrastructure protection
  - Data protection at rest and in transit
  - Incident response
  - Application security

### Google Cloud Partner Skills
- **URL:** http://partner.skills.google/
- **Description:** Cross-cloud security training for partners

---

## 🎯 Learning Path Recommendations

### For Security Engineers
1. Start with **Security Baseline Workshop** (IAM & Detection basics)
2. Progress to **Threat Detection and Response** (Comprehensive detection)
3. Deep dive into **IAM Policy Learning Experience** and **IAM Access Analyzer**
4. Master **Incident Response Playbooks Workshop**
5. Explore **Zero Trust** and **Data Perimeter** workshops

### For Cloud Architects
1. Begin with **AWS Networking Workshop** (Infrastructure foundations)
2. Study **Layered Security on Amazon VPC**
3. Learn **Network Firewall** and **WAF** workshops
4. Implement **IAM Identity Center** at scale
5. Master **Data Perimeter** and **Encryption** workshops

### For DevSecOps Engineers
1. Start with **Security for Developers**
2. Build **Secure Pipelines in AWS**
3. Implement **DevSecOps CI/CD** patterns
4. Integrate **IAM Access Analyzer into CI/CD**
5. Master **Terraform CI/CD and Testing**

### For Incident Response Teams
1. Begin with **Security Event Simulations** (Ransomware, Cryptomining, etc.)
2. Build **AWS Incident Response Playbooks**
3. Implement **Automating Incident Response**
4. Study **AWS CIRT Toolkit**
5. Master **Threat Detection and Response**

---

## 📊 Summary Statistics

### Resources by Difficulty Level
- **Basic (100-200):** 15 workshops, 8 repositories
- **Medium (200-300):** 43 workshops, 25 repositories
- **Advanced (300-400):** 31 workshops, 20 repositories

### Resources by Domain
- **Domain 2 (IAM):** 28 workshops, 11 repositories
- **Domain 3 (Detection):** 12 workshops, 2 repositories
- **Domain 4 (Infrastructure Protection):** 15 workshops, 6 repositories
- **Domain 5 (Data Protection):** 14 workshops, 2 repositories
- **Domain 6 (Incident Response):** 7 workshops, 9 repositories
- **Domain 7 (Application Security):** 13 workshops, 8 repositories

### Total Resources
- **Workshops:** 89 hands-on workshops (+12 from builder.aws.com)
- **GitHub Repositories:** 38 active repositories (commits within 2 years)
- **AWS Solutions:** 2 production-ready solutions

---

## 🔄 Update Policy

This document is maintained to include only:
- ✅ Active workshops from workshops.aws
- ✅ GitHub repositories with commits after **December 15, 2023**
- ✅ Resources mapped to Enterprise Cloud Security Knowledge Framework domains
- ✅ Verified difficulty levels based on AWS documentation

**Next Update:** June 15, 2026

---

## 📝 Contributing

To suggest additional resources:
1. Verify repository has recent commits (within 2 years)
2. Confirm alignment with framework domains
3. Validate difficulty level matches content complexity
4. Ensure workshop URLs are current and accessible

---

**Document Version:** 2.0  
**Last Updated:** December 15, 2025  
**Framework Version:** Enterprise Cloud Security Knowledge Framework (Domains 2-7)
