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

---

## Class Meeting Schedule
<!-- anchor: #class-meeting-schedule -->

| Day | Time | Location | Notes |
|-----|------|----------|-------|
| {Monday} | {h:mm AM} - {h:mm PM} | {Building Room} | {Regular class} |
| {Wednesday} | {h:mm AM} - {h:mm PM} | {Building Room} | {Regular class} |

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

| Assignment ID | Title | Type | Module ID | Due Date (Display) | Due Date (ISO) | Due Time | Points |
|---------------|-------|------|-----------|-------------------|----------------|----------|--------|
| A01 | {Assignment title} | {individual/quiz/discussion/exam/group/presentation} | M01 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |
| A02 | {Assignment title} | {Type} | M02 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |
| A03 | {Assignment title} | {Type} | M03 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |
| QUIZ-01 | {Quiz title} | quiz | M02 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |
| QUIZ-02 | {Quiz title} | quiz | M04 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |
| MIDTERM | Midterm Exam | exam | null | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |
| FINAL | Final Exam | exam | null | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |
| D01 | {Discussion title} | discussion | M01 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |
| D02 | {Discussion title} | discussion | M02 | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {N} |

{Add rows for all assignments, quizzes, exams, and discussions. For TBD dates, use "TBD" for display and leave ISO date as null.}

**Assignment Types:** `individual`, `quiz`, `discussion`, `exam`, `group`, `presentation`

**TBD Example Row:**
| A07 | {Assignment title} | {Type} | M07 | TBD | null | null | {N} |

---

## Milestone Timeline
<!-- anchor: #milestone-timeline -->

{For group projects or multi-phase assignments with tracked milestones.}

| Milestone ID | Title | Project ID | Due Date (Display) | Due Date (ISO) | Due Time | Deliverable |
|--------------|-------|------------|-------------------|----------------|----------|-------------|
| MS01 | {Milestone 1 title} | PROJ-FINAL | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {e.g., "Team formation + topic proposal"} |
| MS02 | {Milestone 2 title} | PROJ-FINAL | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {Deliverable description} |
| MS03 | {Milestone 3 title} | PROJ-FINAL | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {Deliverable description} |
| MS04 | {Milestone 4 - Final} | PROJ-FINAL | {DayOfWeek, Mon DD, YYYY} | {YYYY-MM-DD} | {h:mm AM/PM} | {e.g., "Final presentation + report"} |

{Use PROJ-FINAL-MS01 format if multiple projects exist. For single project, MS01 format is sufficient.}

---

## Weekly Overview
<!-- anchor: #weekly-overview -->

{Optional: Provides a week-by-week summary for pacing reference.}

### Week 1: {Date Range}
- **Module:** M01
- **Topics:** {Topics covered}
- **Due This Week:**
  - {Assignment/Discussion with date}

### Week 2: {Date Range}
- **Module:** M01/M02
- **Topics:** {Topics covered}
- **Due This Week:**
  - {Assignment/Discussion with date}

{Continue for all weeks of the term.}

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
| #assignment-calendar | Assignment Calendar | assignments, exams, discussions, quizzes |
| #milestone-timeline | Milestone Timeline | milestones |
| #weekly-overview | Weekly Overview | — |
| #office-hours-schedule | Office Hours Schedule | — |
| #index-references | Index References | — |

---

## Template Validation Checklist

Before finalizing course_schedule.md, verify:

- [ ] All dates have BOTH display_date AND iso_date fields
- [ ] display_date format: DayOfWeek, Mon DD, YYYY
- [ ] iso_date format: YYYY-MM-DD
- [ ] Day of week matches actual calendar day for all dates
- [ ] All times use h:mm AM/PM format (12-hour, uppercase AM/PM)
- [ ] TBD dates use "TBD" for display and null for ISO
- [ ] Module IDs follow M{NN} pattern (zero-padded)
- [ ] Assignment IDs follow standard patterns (A{NN}, QUIZ-{NN}, D{NN}, MIDTERM, FINAL, etc.)
- [ ] Assignment types are one of: individual, quiz, discussion, exam, group, presentation
- [ ] Milestone IDs follow MS{NN} or {PROJECT_ID}-MS{NN} pattern
- [ ] All entity IDs are unique within their type

---

**END OF COURSE SCHEDULE TEMPLATE**
