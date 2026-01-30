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

This section consolidates ALL assignment types including individual assignments, quizzes, discussions, exams, group projects, and readings. The `Type` field distinguishes different assignment categories.

| Assignment ID | Title | Type | Due Date (Display) | Due Date (ISO) | Due Time | Points | Module ID |
|---------------|-------|------|-------------------|----------------|----------|--------|-----------|
| A01 | {Assignment title} | Individual | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {100} | M01 |
| QUIZ-01 | {Quiz title} | Quiz | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {50} | M02 |
| D01 | {Discussion topic} | Discussion | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {25} | M02 |
| MIDTERM | Midterm Exam | Exam | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {200} | M05 |
| GROUP-01 | {Group project title} | Group | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {150} | M07 |
| M03-R01 | {Reading citation} | Reading | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {0} | M03 |
| FINAL | Final Exam | Exam | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {250} | M10 |

{Add rows for all assignments of any type. For TBD dates, use "TBD" for display and leave ISO date as null.}

**TBD Example Row:**
| A07 | {Assignment title} | Individual | TBD | null | null | {100} | M07 |

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
| #assignment-calendar | Assignment Calendar | assignments, quizzes, discussions, exams, group projects, readings |
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