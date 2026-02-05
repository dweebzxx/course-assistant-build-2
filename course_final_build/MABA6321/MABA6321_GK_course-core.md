# Course Core Template

**Filename Pattern:** `MABA6321_GK_course-core.md`  
**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_GK_course-core\.md$`  
**Authority Tier:** 1 (Highest authority for syllabus, policies, grading, structure, group project)  
**Example Filename:** `MABA6321_GK_course-core.md`

**Purpose:** Contains complete course syllabus, policies, grading structure, instructor information, and group project definition. Tier 1 authority - highest priority for all course requirements. Does NOT contain specific dates and deadlines - see course-schedule.md (Tier 2) for all temporal information.

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `MABA6321` |
| **term_id** | `2026-SP` |
| **course_run_id** | `MABA6321-2026-SP` |
| **doc_type** | `course_core` |
| **last_updated** | `2026-02-05` |
| **timezone** | `America/Chicago` |
| **source_files** | `syllabus.md, export_summary.json` |

**Change Log (optional):**
- 2026-02-05: Initial creation from Canvas export

---

## Course Identification
<!-- anchor: #course-identification -->

| Field | Value |
|-------|-------|
| **Course Title** | Data Management and Big Data |
| **Course Number** | MABA 6321 |
| **Section** | 070 |
| **Credits** | 2 |
| **Term** | Spring 2026 (Jan 20 - Mar 16) |
| **Delivery Mode** | Online Asynchronous |
| **Meeting Pattern** | No designated meeting times (asynchronous) |
| **Location** | Online via Canvas |

---

## Instructor Information
<!-- anchor: #instructor-information -->

| Field | Value |
|-------|-------|
| **Instructor Name** | Dr. De Liu |
| **Email** | deliu@umn.edu |
| **Phone** | Not provided |
| **Office** | Xian Dong Eric Jing Professor, Department of Information and Decision Sciences, Carlson School of Management |
| **Office Hours** | Thursdays 4-5 PM CT via Zoom |
| **Preferred Contact Method** | Slack Chat: https://maba6321spring2026.slack.com (preferred) or Email |
| **Response Time Expectation** | Not specified |

**Teaching Assistants (if applicable):**

| Name | Email | Office Hours | Responsibilities |
|------|-------|--------------|------------------|
| Aditya Bobde | bobde002@umn.edu | Via Slack or Email | PhD Student, Department of Information and Decision Sciences |

---

## Course Syllabus
<!-- anchor: #course-syllabus -->

**Syllabus Overview:**

Data management is the foundation of data-driven enterprises and a cornerstone for business analytics. Organizations store most of their data in a *relational* format. Structured Query Language (SQL), the language for querying and manipulating relational databases, is one of the most important skills for data scientists. Moreover, organizations need to scale their data infrastructure to harness big data, including using parallel processing and cloud computing. Through this course, students will gain competence in practical database, data warehousing, and data management skills with emphasis on query, data modeling, and data management. Students will also be exposed to recent advances in big data technologies and cloud-based data warehousing.

**Key Syllabus Points:**
- SQL is one of the most important skills for data scientists
- Focus on relational databases, data warehousing, and data management
- Exposure to big data technologies and cloud-based data warehousing
- Online asynchronous format with no required meetings

**Syllabus Version:** Spring 2026

---

## Course Description
<!-- anchor: #course-description -->

Data management is the foundation of data-driven enterprises and a cornerstone for business analytics. Organizations store most of their data in a *relational* format. Structured Query Language (SQL), the language for querying and manipulating relational databases, is one of the most important skills for data scientists. Moreover, organizations need to scale their data infrastructure to harness big data, including using parallel processing and cloud computing. Through this course, students will gain competence in practical database, data warehousing, and data management skills with emphasis on query, data modeling, and data management. Students will also be exposed to recent advances in big data technologies and cloud-based data warehousing.

---

## Learning Objectives
<!-- anchor: #learning-objectives -->

Upon successful completion of this course, students will be able to:

1. Gain competence in practical database skills
2. Master SQL for querying and manipulating relational databases
3. Understand data warehousing concepts and practices
4. Apply data modeling techniques
5. Manage data effectively in enterprise settings
6. Understand big data technologies including parallel processing and cloud computing
7. Work with cloud-based data warehousing systems (Snowflake)

---

## Required Resources
<!-- anchor: #required-resources -->

### Textbooks

| Title | Author(s) | Edition | ISBN | Required/Optional |
|-------|-----------|---------|------|-------------------|
| None required | N/A | N/A | N/A | N/A |

There is no required textbook for this course.

### Optional Course Materials

SQL Queries for Mere Mortals: A Hands-On Guide to Data Manipulation in SQL - For most students, the instructor's notes on SQL would be sufficient. This book is recommended for ones who need a reference book for SQL.

### Software and Technology

| Resource | Purpose | Access Instructions |
|----------|---------|---------------------|
| MySQL Community Server | Database software | Install on personal computer |
| MySQL Workbench | Official MySQL GUI client | Install on personal computer |
| Databricks Free Edition | Big Data module | Sign up at https://www.databricks.com/learn/free-edition (no credit card required) |
| Snowflake | Cloud-based data warehousing | Computing environment provided |
| Canvas | Course management | university Canvas |

### Installation Instructions

- Windows: Install MySQL Community Server (8.0.4) and MySQL Workbench (8.0.4) by following this YouTube video: https://www.youtube.com/watch?v=C8cLGUuGsrQ
- Mac: Install MySQL Community Server (8.0.4) and MySQL Workbench (8.0.4) by following this YouTube video: https://www.youtube.com/watch?v=-wpzS5NcYT8

---

## Grading Policy
<!-- anchor: #grading-policy -->

### Grading Components

| Component | Weight | Description |
|-----------|--------|-------------|
| Homework Assignments | 20% | Individual homework assignments |
| Labs | 30% | Hands-on lab exercises |
| Quiz 1 (Modules 1-3) | 20% | Covers modules 1-3 |
| Quiz 2 (Modules 4-5) | 15% | Covers modules 4-5 |
| Quiz 3 (Modules 6-7) | 15% | Covers modules 6-7 |
| **Total** | **100%** | |

### Grading Scale

| Letter Grade | Percentage Range | GPA Points |
|--------------|------------------|------------|
| A | 93.0 or above | 4.0 |
| A- | 90.0 - 92.9 | 3.67 |
| B+ | 87.0 - 89.9 | 3.33 |
| B | 83.0 - 86.9 | 3.0 |
| B- | 80.0 - 82.9 | 2.67 |
| C+ | 77.0 - 79.9 | 2.33 |
| C | 73.0 - 76.9 | 2.0 |
| C- | 70.0 - 72.9 | 1.67 |
| D | 60.0 - 69.9 | 1.0 |
| F | Below 60.0 | 0.0 |

Though it rarely happens, this scale may be adjusted to ensure compliance with Carlson grading policies, which require a class median GPA of 3.3 +/- 0.2.

### Grade Calculation Method

Grades are calculated based on the weighted components listed above.

### Extra Credit

SmartPAL Participation Extra Credit (1%) - Voluntary learning support tool with chatbot, personalized reminders, feedback, and gamification features.

---

## Course Policies
<!-- anchor: #course-policies -->

### Attendance Policy
<!-- anchor: #attendance-policy -->

This course is offered in an online asynchronous format via Canvas, allowing students to access pre-recorded lectures, complete assignments and labs, and take quizzes according to their own pace. While there are no required meetings, students are responsible for adhering to the weekly schedule and actively participating in course activities to remain on track.

**Summary:** No required attendance; students must follow weekly schedule and complete activities on time.

### Participation Policy
<!-- anchor: #participation-policy -->

Students are responsible for adhering to the weekly schedule and actively participating in course activities. As an asynchronous online course, there are no designated meeting times.

### Late Work Policy
<!-- anchor: #late-work-policy -->

**Flex Days for Late Homework Assignments/Labs:**
- You have 5 flex days that you may use at your discretion to defer the due date of a homework assignment or a lab
- You must use flex days in whole day (24 hours) increments
- You can defer a single assignment by a maximum of 2 days
- You do not need to notify the instructor if you want to use your flex days
- Submit your homework/lab when ready and the proper number of flex days will be deducted
- Flex days are intended for unforeseen circumstances such as technical difficulties, family emergencies, and personal illness
- After your flex days have been used for the semester, late work will not be accepted and will earn no credit (0 points)
- Additional accommodations must be obtained in advance

**Summary:** 5 flex days available for homework/labs; max 2 days per assignment; no credit after flex days used.

### Academic Integrity Policy
<!-- anchor: #academic-integrity-policy -->

The Carlson School defines academic misconduct as any act by a student that misrepresents the student's own academic work or that compromises the academic work of another. Scholastic misconduct includes (but is not limited to) cheating on assignments or examinations, plagiarizing, i.e., misrepresenting as one's own work any work done by another, submitting the same paper, or substantially similar papers, to meet the requirement of more than one course without the approval and consent of the instructors concerned, or sabotaging another's work.

**Integrity Related to Homework Assignments:**
- Do all homework assignments individually
- You may discuss homework problems with fellow students
- No documents or fragments of homework should be shared between students, physically or digitally
- Rule of thumb: you should have "typed it with your own hands"
- Always save a copy of your submitted work in a secure location (such as Google Drive)

**AI Use Policy:** Generative AI tools (such as ChatGPT and Copilot) can be valuable resources for enhancing your learning experience. You are encouraged to use Gen AI for non-quiz assignments, including homework assignments, lab problems, and knowledge check questions. The use of Gen AI is strictly forbidden during quizzes. Using Gen AI during quizzes is considered a breach of academic integrity and may result in grading penalty and disciplinary actions.

When using Gen AI:
- Always verify and refine the generated content to ensure accuracy
- Take time to understand generative AI output and be ready to explain it in your own words
- Incorporate your own ideas and perspectives instead of relying entirely on generative AI

### Accommodation Policy
<!-- anchor: #accommodation-policy -->

The University of Minnesota is committed to providing all students equal access to learning opportunities. The Disability Resource Center (DRC) is the campus office that works with students who have disabilities to provide and/or arrange reasonable accommodations. Students registered with the DRC, who have a letter requesting accommodations, are encouraged to contact the instructor early in the semester. Students who have, or think they may have, a disability (e.g. psychiatric, attention, learning, vision, hearing, physical, or systemic), are invited to contact the DRC for a confidential discussion at 612-626-1333 (V/TTY) or at drc@umn.edu. Additional information is available on the Disability Resource Center website at https://z.umn.edu/disability_resource_center.

---

## Assignment Specifications
<!-- anchor: #assignment-specifications -->

### Submission Requirements

| Requirement | Specification |
|-------------|---------------|
| **Submission Platform** | Canvas |
| **File Format** | As specified per assignment |
| **Naming Convention** | Not specified |
| **Late Submission Method** | Use flex days (up to 2 days per assignment) |

### Assignment Types Overview

#### Homework Assignments

Homework assignments cover the topics in each module with a focus on relational database concepts and SQL queries.

- **Number of Assignments:** 3 (Homework 1, 2, 3)
- **Format:** Individual
- **Evaluation:** Points-based

#### Labs

Hands-on lab exercises to practice database skills.

- **Number of Labs:** 5+ (Labs 1-5 for SQL, ER Diagrams, Normalization)
- **Format:** Hands-on exercises using MySQL Workbench
- **Evaluation:** Points-based

#### Quizzes

All quizzes will be conducted on Canvas and will consist of multiple-choice and/or short answers. There will not be hands-on SQL scripting.

- **Number of Quizzes:** 3
- **Format:** Multiple choice and/or short answers on Canvas
- **Duration:** 60 minutes (for Quiz 1)
- **Proctoring:** HonorLock required
- **Open/Closed Resources:** No external resources, no communication tools allowed

---

## Communication Guidelines
<!-- anchor: #communication-guidelines -->

### Contacting the Instructor

- **For general questions:** Slack Workspace (https://maba6321spring2026.slack.com) - preferred
- **For personal/grade concerns:** Email or Slack
- **For urgent matters:** Email (deliu@umn.edu)
- **Expected response time:** Not specified

### Course Announcements

- **Primary channel:** Canvas Announcements
- **Frequency:** As needed
- **Student responsibility:** Set "Announcements" delivery to "Notify immediately" in Canvas communication settings

### Slack Workspace

We will use a Slack Workspace (https://maba6321spring2026.slack.com) for community-based interaction and day-to-day Q&A & support. We recommend that you install it on your mobile device and/or connect with the class community.

---

## University Policies Reference
<!-- anchor: #university-policies-reference -->

- Academic integrity: https://z.umn.edu/policy-carlson_student_conduct_code
- Student conduct code: https://z.umn.edu/policy-student_conduct_code
- Disability accommodations: https://z.umn.edu/disability_resource_center
- Title IX: https://z.umn.edu/title_ix_process
- Mental health resources: https://z.umn.edu/mental_health_services
- Writing support: https://z.umn.edu/student_writing_support
- Make-up work policy: https://z.umn.edu/policy-makeup_work

---

## Group Project Context
<!-- anchor: #group-project-context -->

### Course-Level Project Definition

| Field | Value |
|-------|-------|
| **Group Project Required** | No |
| **Project ID** | N/A |
| **Project Scope** | N/A |
| **Team Size** | N/A |

### Student Assignment (Josh)

| Field | Value |
|-------|-------|
| **Assigned to Group Project** | No |
| **Team Name** | N/A |
| **Josh's Role** | N/A |

---

## Index References
<!-- anchor: #index-references -->

This file contains the following sections indexed for retrieval:

| Section Anchor | Section Title | Entity IDs |
|----------------|---------------|------------|
| #metadata | Metadata | — |
| #course-identification | Course Identification | — |
| #instructor-information | Instructor Information | — |
| #course-syllabus | Course Syllabus | — |
| #course-description | Course Description | — |
| #learning-objectives | Learning Objectives | — |
| #required-resources | Required Resources | — |
| #grading-policy | Grading Policy | — |
| #course-policies | Course Policies | — |
| #attendance-policy | Attendance Policy | — |
| #participation-policy | Participation Policy | — |
| #late-work-policy | Late Work Policy | — |
| #academic-integrity-policy | Academic Integrity Policy | — |
| #accommodation-policy | Accommodation Policy | — |
| #assignment-specifications | Assignment Specifications | — |
| #communication-guidelines | Communication Guidelines | — |
| #university-policies-reference | University Policies Reference | — |
| #group-project-context | Group Project Context | — |
| #index-references | Index References | — |

---

**END OF COURSE CORE**
