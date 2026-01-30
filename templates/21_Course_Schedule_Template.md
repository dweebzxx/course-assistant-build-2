# Course Schedule Template

**Template Number:** 21  
**Document Type:** Grounded Knowledge File Template  
**Phase:** 4  
**Date:** 2026-01-25  
**Status:** Definitive template for course_schedule.md

---

## Overview

This template provides the structure for the Course Schedule Grounded Knowledge File (`{course_id}.course_schedule.md`), which serves as Tier 1 authority for all dates, times, and deadlines. This file is required for every agent build.

Use exactly the section headers and anchor IDs shown below to ensure INDEX compatibility and retrieval accuracy.

---

# Course Schedule Template

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