# Course Knowledge Templates

**Document Type:** Grounded Knowledge File Templates  
**Phase:** 4  
**Date:** 2026-01-25  
**Status:** Definitive templates for course_core.md and course_schedule.md

---

## Overview

This document provides fillable templates for the two course-level Grounded Knowledge Files:

1. **Part A: Course Core Template** (`{course_id}.course_core.md`) — Tier 2 authority for policies, grading, and structure
2. **Part B: Course Schedule Template** (`{course_id}.course_schedule.md`) — Tier 1 authority for all dates and deadlines

Both files are required for every agent build. Use exactly the section headers and anchor IDs shown below to ensure INDEX compatibility and retrieval accuracy.

---

# PART A: Course Core Template

**Filename Pattern:** `{course_id}.course_core.md`  
**Regex:** `^[A-Z0-9\-]+\.course_core\.md$`  
**Authority Tier:** 2 (Authoritative for policies, grading, structure)  
**Example Filename:** `MGMT-5001-SEC01-2026-SP.course_core.md`

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `{COURSE_ID}` |
| **term_id** | `{YYYY}-{TT}` |
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
| #index-references | Index References | — |

---

**END OF COURSE CORE TEMPLATE**

---
---
---

# PART B: Course Schedule Template

**Filename Pattern:** `{course_id}.course_schedule.md`  
**Regex:** `^[A-Z0-9\-]+\.course_schedule\.md$`  
**Authority Tier:** 1 (Authoritative for ALL dates, times, and deadlines)  
**Example Filename:** `MGMT-5001-SEC01-2026-SP.course_schedule.md`

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `{COURSE_ID}` |
| **term_id** | `{YYYY}-{TT}` |
| **doc_type** | `course_schedule` |
| **last_updated** | `{YYYY-MM-DD}` |
| **timezone** | `America/Chicago` |
| **source_files** | `{comma-separated list of original source filenames}` |

**Change Log (optional):**
- {YYYY-MM-DD}: {Description of change}

---

## Term Dates
<!-- anchor: #term-dates -->

| Milestone | Display Date | ISO Date |
|-----------|--------------|----------|
| **Term Start** | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} |
| **Term End** | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} |
| **Classes Begin** | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} |
| **Classes End** | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} |
| **Finals Period Start** | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} |
| **Finals Period End** | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} |

### Academic Calendar Events

| Event | Display Date | ISO Date | Notes |
|-------|--------------|----------|-------|
| {Holiday/Break name} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {e.g., "No class"} |
| {Spring Break Start} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Notes} |
| {Spring Break End} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Notes} |
| {Add/Drop Deadline} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Notes} |
| {Withdrawal Deadline} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Notes} |

---

## Class Meeting Schedule
<!-- anchor: #class-meeting-schedule -->

| Day | Time | Location | Notes |
|-----|------|----------|-------|
| {Monday} | {h:mm AM} - {h:mm PM} | {Building Room} | {Regular class} |
| {Wednesday} | {h:mm AM} - {h:mm PM} | {Building Room} | {Regular class} |

**Exceptions to Regular Schedule:**

| Date (Display) | Date (ISO) | Change Description |
|----------------|------------|-------------------|
| {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {e.g., "Class cancelled - instructor travel"} |
| {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {e.g., "Room change to Building XYZ"} |

---

## Module Sequence
<!-- anchor: #module-sequence -->

| Module ID | Module Title | Start Date (Display) | Start Date (ISO) | End Date (Display) | End Date (ISO) | Topics |
|-----------|--------------|----------------------|------------------|-------------------|----------------|--------|
| M01 | {Module 1 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M02 | {Module 2 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M03 | {Module 3 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M04 | {Module 4 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M05 | {Module 5 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M06 | {Module 6 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M07 | {Module 7 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M08 | {Module 8 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M09 | {Module 9 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |
| M10 | {Module 10 Title} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Topic list} |

{Add or remove rows as needed. Use TBD for dates not yet announced with null ISO dates.}

---

## Assignment Calendar
<!-- anchor: #assignment-calendar -->

| Assignment ID | Title | Type | Module ID | Due Date (Display) | Due Date (ISO) | Due Time | Weight | Notes |
|---------------|-------|------|-----------|-------------------|----------------|----------|--------|-------|
| A01 | {Assignment title} | {Individual/Quiz/etc.} | M01 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {X%} | {Notes} |
| A02 | {Assignment title} | {Type} | M02 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {X%} | {Notes} |
| A03 | {Assignment title} | {Type} | M03 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {X%} | {Notes} |
| QUIZ-01 | {Quiz title} | Quiz | M02 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {X%} | {Notes} |
| QUIZ-02 | {Quiz title} | Quiz | M04 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {X%} | {Notes} |

{Add rows for all assignments. For TBD dates, use "TBD" for display and leave ISO date as null.}

**TBD Example Row:**
| A07 | {Assignment title} | {Type} | M07 | TBD | null | null | {X%} | Due date not yet announced |

---

## Exam Schedule
<!-- anchor: #exam-schedule -->

| Exam ID | Title | Date (Display) | Date (ISO) | Time | Duration | Location | Format | Materials Allowed |
|---------|-------|----------------|------------|------|----------|----------|--------|-------------------|
| MIDTERM | Midterm Exam | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {X hours} | {Location} | {In-class/Online} | {List or "None"} |
| FINAL | Final Exam | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {X hours} | {Location} | {Format} | {List or "None"} |

{Add rows for any additional exams. Use EXAM-01, EXAM-02 for numbered exams.}

---

## Reading Schedule
<!-- anchor: #reading-schedule -->

| Reading ID | Title/Citation | Module ID | Due Date (Display) | Due Date (ISO) | Notes |
|------------|----------------|-----------|-------------------|----------------|-------|
| M01-R01 | {Reading title or citation} | M01 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {e.g., "Read before class"} |
| M01-R02 | {Reading title or citation} | M01 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Notes} |
| M02-R01 | {Reading title or citation} | M02 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Notes} |
| M03-R01 | {Reading title or citation} | M03 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {Notes} |

{Add rows for all required readings. Use module-scoped IDs (M{NN}-R{NN}) when readings are organized by module.}

---

## Discussion Schedule
<!-- anchor: #discussion-schedule -->

| Discussion ID | Title/Topic | Module ID | Open Date (Display) | Open Date (ISO) | Open Time | Close Date (Display) | Close Date (ISO) | Close Time | Requirements |
|---------------|-------------|-----------|---------------------|-----------------|-----------|---------------------|------------------|------------|--------------|
| D01 | {Discussion topic} | M01 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {e.g., "Initial post + 2 replies"} |
| D02 | {Discussion topic} | M02 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {Requirements} |

{Add rows for all discussion assignments. Include both open and close dates/times.}

---

## Milestone Timeline
<!-- anchor: #milestone-timeline -->

{For group projects or multi-phase assignments with tracked milestones.}

| Milestone ID | Title | Project ID | Due Date (Display) | Due Date (ISO) | Due Time | Deliverable | Weight (of Project) |
|--------------|-------|------------|-------------------|----------------|----------|-------------|---------------------|
| MS01 | {Milestone 1 title} | PROJ-FINAL | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {e.g., "Team formation + topic proposal"} | {X%} |
| MS02 | {Milestone 2 title} | PROJ-FINAL | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {Deliverable description} | {X%} |
| MS03 | {Milestone 3 title} | PROJ-FINAL | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {Deliverable description} | {X%} |
| MS04 | {Milestone 4 - Final} | PROJ-FINAL | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {e.g., "Final presentation + report"} | {X%} |

{Use PROJ-FINAL-MS01 format if multiple projects exist. For single project, MS01 format is sufficient.}

---

## Weekly Overview
<!-- anchor: #weekly-overview -->

{Optional: Provides a week-by-week summary for pacing reference.}

### Week 1: {Date Range}
- **Module:** M01
- **Topics:** {Topics covered}
- **Due This Week:**
  - {Assignment/Reading/Discussion with date}
  - {Assignment/Reading/Discussion with date}

### Week 2: {Date Range}
- **Module:** M01/M02
- **Topics:** {Topics covered}
- **Due This Week:**
  - {Assignment/Reading/Discussion with date}

{Continue for all weeks of the term.}

---

## Special Events
<!-- anchor: #special-events -->

| Event | Date(s) | Time | Location | Description | Required? |
|-------|---------|------|----------|-------------|-----------|
| {Guest speaker} | {DayOfWeek, Mon DD, YYYY} | {h:mm AM/PM} | {Location} | {Description} | {Yes/No/Extra credit} |
| {Workshop} | {Start Date} to {End Date} | {Time} | {Location} | {Description} | {Yes/No} |
| {Field trip} | {DayOfWeek, Mon DD, YYYY} | {Time} | {Location} | {Description} | {Yes/No} |

{Include any special events, guest lectures, workshops, or field activities.}

---

## Office Hours Schedule
<!-- anchor: #office-hours-schedule -->

| Day | Time | Location | Format | Notes |
|-----|------|----------|--------|-------|
| {Tuesday} | {h:mm AM/PM} - {h:mm AM/PM} | {Office/Zoom} | {In-person/Virtual/Hybrid} | {e.g., "No appointment needed"} |
| {Thursday} | {h:mm AM/PM} - {h:mm AM/PM} | {Office/Zoom} | {Format} | {Notes} |

**By Appointment:** {Yes/No - include scheduling instructions if yes}

---

## Index References
<!-- anchor: #index-references -->

This file contains the following sections indexed for retrieval:

| Section Anchor | Section Title | Entity Types |
|----------------|---------------|--------------|
| #metadata | Metadata | — |
| #term-dates | Term Dates | — |
| #class-meeting-schedule | Class Meeting Schedule | — |
| #module-sequence | Module Sequence | modules |
| #assignment-calendar | Assignment Calendar | assignments |
| #exam-schedule | Exam Schedule | exams |
| #reading-schedule | Reading Schedule | readings |
| #discussion-schedule | Discussion Schedule | discussions |
| #milestone-timeline | Milestone Timeline | milestones |
| #weekly-overview | Weekly Overview | — |
| #special-events | Special Events | — |
| #office-hours-schedule | Office Hours Schedule | — |
| #index-references | Index References | — |

---

**END OF COURSE SCHEDULE TEMPLATE**

---

## Template Validation Checklist

Before finalizing course knowledge files, verify:

### Course Core Validation
- [ ] course_id matches naming convention (uppercase, alphanumeric, hyphens)
- [ ] term_id follows YYYY-TT format
- [ ] All section headers have corresponding HTML comment anchors
- [ ] Grading components sum to 100%
- [ ] All policy sections are populated (or marked "Not specified in syllabus")
- [ ] No placeholder values remain (all `{brackets}` filled or marked TBD)

### Course Schedule Validation
- [ ] All dates have BOTH display_date AND iso_date fields
- [ ] display_date format: DayOfWeek, Mon DD, YYYY
- [ ] iso_date format: YYYY-MM-DD
- [ ] Day of week matches actual calendar day for all dates
- [ ] All times use h:mm AM/PM format (12-hour, uppercase AM/PM)
- [ ] TBD dates use "TBD" for display and null for ISO
- [ ] Module IDs follow M{NN} pattern (zero-padded)
- [ ] Assignment IDs follow standard patterns (A{NN}, QUIZ-{NN}, etc.)
- [ ] Exam IDs follow standard patterns (MIDTERM, FINAL, EXAM-{NN})
- [ ] All entity IDs are unique within their type
- [ ] Milestone IDs follow MS{NN} or {PROJECT_ID}-MS{NN} pattern

---

**END OF COURSE KNOWLEDGE TEMPLATES DOCUMENT**