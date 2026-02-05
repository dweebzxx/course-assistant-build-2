# Course Schedule Template

**Filename Pattern:** `{course_run_id}.course_schedule.md`  
**Regex:** `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA|SP|SU|WI)\.course_schedule\.md$`  
**Authority Tier:** 1 (Authoritative for ALL dates, times, and deadlines)  
**Example Filename:** `MGMT6022-2026-SP.course_schedule.md`

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `{COURSE_ID}` |
| **term_id** | `{YYYY}-{TT}` |
| **course_run_id** | `{COURSE_ID}-{YYYY}-{TT}` |
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

| Day | Time | Format |
|-----|------|--------|
| {Monday} | {h:mm AM} - {h:mm PM} | {In-person / Online} |
| {Wednesday} | {h:mm AM} - {h:mm PM} | {In-person / Online} |

**Format Options:** `In-person`, `Online`, `Hybrid`

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

| Day | Time | Format |
|-----|------|--------|
| {Tuesday} | {h:mm AM/PM} - {h:mm AM/PM} | {In-person / Online} |
| {Thursday} | {h:mm AM/PM} - {h:mm AM/PM} | {In-person / Online} |

**By Appointment:** {Yes/No - include scheduling instructions if yes}

**Format Options:** `In-person`, `Online`, `Hybrid`

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
| #weekly-overview | Weekly Overview | — |
| #office-hours-schedule | Office Hours Schedule | — |
| #index-references | Index References | — |

---

## Template Validation Checklist

Before finalizing course_schedule.md, verify:

- [ ] course_id matches naming convention (e.g., MGMT6022)
- [ ] term_id follows YYYY-TT format (e.g., 2026-SP)
- [ ] course_run_id follows pattern: {course_id}-{term_id}
- [ ] All dates have BOTH display_date AND iso_date fields
- [ ] display_date format: DayOfWeek, Mon DD, YYYY
- [ ] iso_date format: YYYY-MM-DD
- [ ] Day of week matches actual calendar day for all dates
- [ ] All times use h:mm AM/PM format (12-hour, uppercase AM/PM)
- [ ] TBD dates use "TBD" for display and null for ISO
- [ ] Module IDs follow M{NN} pattern (zero-padded)
- [ ] Assignment IDs follow standard patterns (A{NN}, QUIZ-{NN}, D{NN}, MIDTERM, FINAL, etc.)
- [ ] Assignment types are one of: individual, quiz, discussion, exam, group, presentation
- [ ] All entity IDs are unique within their type

---

**END OF COURSE SCHEDULE TEMPLATE**
