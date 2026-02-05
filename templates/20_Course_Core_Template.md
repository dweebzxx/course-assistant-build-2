# Course Core Template

**Filename Pattern:** `{course_id}_GK_course-core.md`  
**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_GK_course-core\.md$`  
**Authority Tier:** 1 (Highest authority for syllabus, policies, grading, structure, group project)  
**Example Filename:** `MGMT6022_GK_course-core.md`

**Purpose:** Contains complete course syllabus, policies, grading structure, instructor information, and group project definition. Tier 1 authority - highest priority for all course requirements. Does NOT contain specific dates and deadlines - see course-schedule.md (Tier 2) for all temporal information.

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `{COURSE_ID}` |
| **term_id** | `{YYYY}-{TT}` |
| **course_run_id** | `{COURSE_ID}-{YYYY}-{TT}` |
| **doc_type** | `course_core` |
| **last_updated** | `{YYYY-MM-DD}` |
| **timezone** | `America/Chicago` |
| **source_files** | `{comma-separated list of original source filenames}` |

**Change Log (optional):**
- {YYYY-MM-DD}: {Description of change}

---

## Course Identification
<!-- anchor: #course-identification -->

| Field | Value |
|-------|-------|
| **Course Title** | {Full course title} |
| **Course Number** | {Course number, e.g., MGMT 5001} |
| **Section** | {Section identifier, e.g., 001 or SEC01} |
| **Credits** | {Number of credits} |
| **Term** | {Term name, e.g., Spring 2026} |
| **Delivery Mode** | {In-person / Online / Hybrid} |
| **Meeting Pattern** | {Days and times, e.g., MW 2:00 PM - 3:30 PM} |
| **Location** | {Building and room, or "Online"} |

---

## Instructor Information
<!-- anchor: #instructor-information -->

| Field | Value |
|-------|-------|
| **Instructor Name** | {Full name with title} |
| **Email** | {Email address} |
| **Phone** | {Phone number or "Not provided"} |
| **Office** | {Office location} |
| **Office Hours** | {Days, times, and format} |
| **Preferred Contact Method** | {Email / Canvas message / etc.} |
| **Response Time Expectation** | {e.g., "Within 24-48 hours on business days"} |

**Teaching Assistants (if applicable):**

| Name | Email | Office Hours | Responsibilities |
|------|-------|--------------|------------------|
| {TA Name or "None"} | {Email} | {Hours} | {Responsibilities} |

---

## Course Syllabus
<!-- anchor: #course-syllabus -->

**Syllabus Overview:**

{Include the complete course syllabus content here. This section should contain all syllabus information including course overview, expectations, requirements, and any syllabus-specific policies. This is the authoritative source for syllabus content.}

**Key Syllabus Points:**
- {Major syllabus point 1}
- {Major syllabus point 2}
- {Major syllabus point 3}

**Syllabus Version:** {Version number if applicable, e.g., "v1.0" or "Updated 2026-01-15"}

---

## Course Description
<!-- anchor: #course-description -->

{Paste or summarize the official course description from the syllabus. This section provides context for the course content and approach.}

---

## Learning Objectives
<!-- anchor: #learning-objectives -->

Upon successful completion of this course, students will be able to:

1. {Learning objective 1}
2. {Learning objective 2}
3. {Learning objective 3}
4. {Learning objective 4}
5. {Learning objective 5}
{Add or remove objectives as provided in syllabus}

---

## Required Resources
<!-- anchor: #required-resources -->

### Textbooks

| Title | Author(s) | Edition | ISBN | Required/Optional |
|-------|-----------|---------|------|-------------------|
| {Book title} | {Author(s)} | {Edition or "N/A"} | {ISBN or "N/A"} | {Required / Optional / Recommended} |

### Software and Technology

| Resource | Purpose | Access Instructions |
|----------|---------|---------------------|
| {Software/tool name} | {What it's used for} | {How to access, e.g., "Free via university license"} |
| Canvas | Course management | {Canvas URL or "university Canvas"} |

### Other Required Materials

- {List any other required materials}
- {Or state "None" if not applicable}

---

## Grading Policy
<!-- anchor: #grading-policy -->

### Grading Components

| Component | Weight | Description |
|-----------|--------|-------------|
| {Component name, e.g., "Individual Assignments"} | {XX%} | {Brief description} |
| {Component name, e.g., "Quizzes"} | {XX%} | {Brief description} |
| {Component name, e.g., "Midterm Exam"} | {XX%} | {Brief description} |
| {Component name, e.g., "Final Exam"} | {XX%} | {Brief description} |
| {Component name, e.g., "Group Project"} | {XX%} | {Brief description} |
| {Component name, e.g., "Participation"} | {XX%} | {Brief description} |
| **Total** | **100%** | |

### Grading Scale

| Letter Grade | Percentage Range | GPA Points |
|--------------|------------------|------------|
| A | {93-100%} | {4.0} |
| A- | {90-92%} | {3.67} |
| B+ | {87-89%} | {3.33} |
| B | {83-86%} | {3.0} |
| B- | {80-82%} | {2.67} |
| C+ | {77-79%} | {2.33} |
| C | {73-76%} | {2.0} |
| C- | {70-72%} | {1.67} |
| D+ | {67-69%} | {1.33} |
| D | {60-66%} | {1.0} |
| F | {Below 60%} | {0.0} |

{Adjust scale as provided in syllabus. Note any pass/fail options or S/N grading if applicable.}

### Grade Calculation Method

{Describe how final grades are calculated, including any rounding rules, minimum thresholds for passing, or weighted category requirements.}

---

## Course Policies
<!-- anchor: #course-policies -->

### Attendance Policy
<!-- anchor: #attendance-policy -->

{Describe the attendance policy in full. Include:}
- Required attendance expectations
- How attendance is tracked
- Consequences of absences
- Excused vs. unexcused absences
- Maximum allowed absences

**Summary:** {One-sentence summary, e.g., "Attendance is required; more than 3 unexcused absences may result in grade reduction."}

### Participation Policy
<!-- anchor: #participation-policy -->

{Describe how participation is defined, evaluated, and weighted. Include:}
- What counts as participation
- How participation is graded
- Expectations for in-class vs. online participation

### Late Work Policy
<!-- anchor: #late-work-policy -->

{Describe the late work policy in full. Include:}
- Whether late work is accepted
- Penalty structure (e.g., "10% per day")
- Maximum late period
- Exceptions or extension procedures

**Summary:** {One-sentence summary, e.g., "Late work accepted up to 48 hours with 10% penalty per day; no credit after 48 hours."}

### Academic Integrity Policy
<!-- anchor: #academic-integrity-policy -->

{Describe academic integrity expectations. Include:}
- Definition of academic dishonesty for this course
- Collaboration rules (what is allowed vs. prohibited)
- Citation requirements
- AI/technology use policy (if specified)
- Consequences for violations
- Reference to university honor code

**AI Use Policy:** {Explicitly state the instructor's policy on AI tools like ChatGPT, if provided. If not specified, state "Not specified in syllabus."}

### Accommodation Policy
<!-- anchor: #accommodation-policy -->

{Describe the process for requesting accommodations. Include:}
- Contact information for disability services
- Procedures for requesting accommodations
- Timeline for requests

---

## Assignment Specifications
<!-- anchor: #assignment-specifications -->

{This section provides general specifications that apply across assignments. Specific due dates are in course_schedule.md.}

### Submission Requirements

| Requirement | Specification |
|-------------|---------------|
| **Submission Platform** | {Canvas / Email / Other} |
| **File Format** | {PDF / Word / Other} |
| **Naming Convention** | {e.g., "LastName_AssignmentName.pdf"} |
| **Late Submission Method** | {Same as regular / Email to instructor / Not accepted} |

### Assignment Types Overview

#### Individual Assignments

{Describe the general nature, expectations, and evaluation criteria for individual assignments.}

- **Number of Assignments:** {X}
- **Average Length/Scope:** {e.g., "2-3 pages" or "Problem sets with 10-15 questions"}
- **Evaluation Criteria:** {Brief description}

#### Quizzes

{Describe quiz format and expectations.}

- **Number of Quizzes:** {X}
- **Format:** {Multiple choice / Short answer / Mixed}
- **Duration:** {e.g., "30 minutes"}
- **Open/Closed Resources:** {Open book / Closed book / Specific resources allowed}

#### Exams

{Describe exam format and expectations.}

- **Number of Exams:** {X, e.g., "1 Midterm, 1 Final"}
- **Format:** {Description of exam format}
- **Duration:** {e.g., "2 hours"}
- **Location:** {In-class / Online / Testing center}
- **Materials Allowed:** {List allowed materials}

#### Group Project

{Describe group project if applicable. Details on team structure belong in student_profile.md.}

- **Project Scope:** {Brief description}
- **Team Size:** {e.g., "4-5 students"}
- **Number of Milestones:** {X}
- **Final Deliverable:** {Description}

---

## Communication Guidelines
<!-- anchor: #communication-guidelines -->

### Contacting the Instructor

{Describe preferred contact methods and expectations.}

- **For general questions:** {Method}
- **For personal/grade concerns:** {Method}
- **For urgent matters:** {Method}
- **Expected response time:** {Timeframe}

### Course Announcements

{Describe how announcements will be communicated.}

- **Primary channel:** {Canvas announcements / Email / etc.}
- **Frequency:** {e.g., "Weekly" or "As needed"}
- **Student responsibility:** {e.g., "Check Canvas daily"}

---

## University Policies Reference
<!-- anchor: #university-policies-reference -->

{List references to university-wide policies that apply to the course.}

- Academic integrity: {Link or reference}
- Student conduct code: {Link or reference}
- Disability accommodations: {Link or reference}
- Title IX: {Link or reference}
- Mental health resources: {Link or reference}

---

## Group Project Context
<!-- anchor: #group-project-context -->

{This section defines whether a group project is required for the course and its basic identification, plus the student's assignment details.}

### Course-Level Project Definition

| Field | Value |
|-------|-------|
| **Group Project Required** | Yes / No |
| **Project ID** | {Assignment name/ID if yes, e.g., PROJ-FINAL or GP01, or N/A} |
| **Project Scope** | {Brief description of the project} |
| **Team Size** | {e.g., "4-5 students"} |

### Student Assignment (Josh)

| Field | Value |
|-------|-------|
| **Assigned to Group Project** | Yes / No |
| **Team Name** | {Team name if assigned, or N/A} |
| **Josh's Role** | {e.g., Data Analysis Lead, or N/A} |

{Note: Milestone dates and deadlines are in course_schedule.md.}

---

## Index References
<!-- anchor: #index-references -->

This file contains the following sections indexed for retrieval:

| Section Anchor | Section Title | Entity IDs |
|----------------|---------------|------------|
| #metadata | Metadata | — |
| #course-identification | Course Identification | — |
| #instructor-information | Instructor Information | — |
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
| #group-project-context | Group Project Context | {PROJECT_ID} |
| #index-references | Index References | — |

---

## Template Validation Checklist

Before finalizing course_core.md, verify:

- [ ] course_id matches naming convention (e.g., MGMT6022)
- [ ] term_id follows YYYY-TT format (e.g., 2026-SP)
- [ ] course_run_id follows pattern: {course_id}-{term_id}
- [ ] All section headers have corresponding HTML comment anchors
- [ ] Grading components sum to 100%
- [ ] All policy sections are populated (or marked "Not specified in syllabus")
- [ ] No placeholder values remain (all `{brackets}` filled or marked TBD)
- [ ] Group Project Context is completed (Yes/No selection, team name and project ID if applicable)

---

**END OF COURSE CORE TEMPLATE**