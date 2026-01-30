# Date and Time Standard

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Date and time formatting specification  
**Date:** 2026-01-25  
**Phase:** 3  
**Status:** Definitive specification

---

## PURPOSE

This document defines the mandatory date and time formatting standards for all Grounded Knowledge Files, INDEX entries, and agent responses. Consistent, machine-parseable date/time formats are critical for accurate retrieval, pacing, and deadline tracking.

---

## CORE PRINCIPLE: DUAL DATE FIELDS

**All date references MUST include TWO date fields:**

1. **`display_date`:** Human-readable format for agent responses and user-facing output
2. **`iso_date`:** Machine-parseable ISO 8601 format for sorting, filtering, and validation

**Exception:** Metadata fields like `last_updated` use ISO date only (YYYY-MM-DD).

---

## DATE FIELD STANDARDS

### display_date Format

**Pattern:** `DayOfWeek, Mon DD, YYYY`

**Components:**
- `DayOfWeek`: Full day name (Monday, Tuesday, ..., Sunday)
- `Mon`: Three-letter month abbreviation (Jan, Feb, ..., Dec)
- `DD`: Two-digit zero-padded day (01, 02, ..., 31)
- `YYYY`: Four-digit year

**Examples:**
- `Monday, Jan 20, 2026`
- `Friday, Feb 14, 2026`
- `Sunday, Dec 31, 2025`

**Regex:** `^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (0[1-9]|[12][0-9]|3[01]), (20\d{2})$`

**Validation:**
- Day of week MUST match the actual day for the given date
- Day number must be valid for the given month/year (e.g., Feb 30 is invalid)

---

### iso_date Format

**Pattern:** `YYYY-MM-DD`

**Components:**
- `YYYY`: Four-digit year
- `MM`: Two-digit zero-padded month (01, 02, ..., 12)
- `DD`: Two-digit zero-padded day (01, 02, ..., 31)

**Examples:**
- `2026-01-20`
- `2026-02-14`
- `2025-12-31`

**Regex:** `^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$`

**Validation:**
- Must be valid ISO 8601 date
- Day must be valid for month/year

---

## TIME FIELD STANDARDS

### Standard Time Format: 12-Hour with AM/PM

**Pattern:** `h:mm AM` or `h:mm PM`

**Components:**
- `h`: Hour (1-12, no leading zero for single-digit hours)
- `mm`: Two-digit zero-padded minutes (00-59)
- `AM` or `PM`: Required (uppercase, no periods)

**Examples:**
- `9:00 AM`
- `11:59 PM`
- `2:30 PM`
- `12:00 PM` (noon)
- `12:00 AM` (midnight)

**Regex:** `^(1[0-2]|[1-9]):[0-5][0-9] (AM|PM)$`

**Validation:**
- Hour must be 1-12 (not 0 or 13+)
- Minutes must be 00-59
- AM/PM required, uppercase, no periods

---

### Edge Cases: Noon and Midnight

**Noon:**
- `12:00 PM` (correct)
- NOT `12:00 AM`

**Midnight:**
- `12:00 AM` (correct, start of day)
- `11:59 PM` (last minute of day, preferred for end-of-day deadlines)

**Best practice for assignment deadlines:**
- Use `11:59 PM` for "end of day" deadlines
- Avoid `12:00 AM` to prevent ambiguity (is it start or end of day?)

---

## TIMEZONE STANDARD

### Primary Timezone Format: IANA Timezone Name

**Preferred:** `America/Chicago`

**Why:** IANA timezone names handle Daylight Saving Time automatically and are unambiguous.

### Acceptable Abbreviation: Two-Letter Code

**Acceptable:** `CT` (for Central Time)

**Use when:**
- Space is limited
- Context is already established (e.g., all course dates are CT)

**Avoid:** `CST` / `CDT` unless absolutely necessary (adds complexity for DST transitions)

---

## COMPLETE DATE-TIME EXAMPLES

### Assignment Due Date (with time)

**Markdown:**
```markdown
- **Due Date (display):** Monday, Feb 10, 2026
- **Due Date (ISO):** 2026-02-10
- **Due Time:** 11:59 PM
- **Timezone:** America/Chicago
```

**JSON (in INDEX):**
```json
{
  "entity_id": "A03",
  "due_date_display": "Monday, Feb 10, 2026",
  "due_date_iso": "2026-02-10",
  "due_time": "11:59 PM",
  "timezone": "America/Chicago"
}
```

**Agent Response:**
```
Assignment A03 is due Monday, Feb 10, 2026 at 11:59 PM CT.
Source: course_schedule.md#assignment-calendar (A03)
```

---

### Exam Date and Time

**Markdown:**
```markdown
- **Exam Date (display):** Wednesday, Mar 05, 2026
- **Exam Date (ISO):** 2026-03-05
- **Exam Time:** 2:00 PM
- **Timezone:** America/Chicago
```

**JSON:**
```json
{
  "entity_id": "EXAM-MIDTERM",
  "due_date_display": "Wednesday, Mar 05, 2026",
  "due_date_iso": "2026-03-05",
  "due_time": "2:00 PM",
  "timezone": "America/Chicago"
}
```

**Agent Response:**
```
The midterm exam is on Wednesday, Mar 05, 2026 at 2:00 PM CT.
Source: course_schedule.md#exam-schedule (EXAM-MIDTERM)
```

---

### Module Date Range (no time)

**Markdown:**
```markdown
- **Start Date (display):** Monday, Feb 03, 2026
- **Start Date (ISO):** 2026-02-03
- **End Date (display):** Sunday, Feb 09, 2026
- **End Date (ISO):** 2026-02-09
```

**JSON:**
```json
{
  "entity_id": "M03",
  "start_date_display": "Monday, Feb 03, 2026",
  "start_date_iso": "2026-02-03",
  "end_date_display": "Sunday, Feb 09, 2026",
  "end_date_iso": "2026-02-09"
}
```

**Agent Response:**
```
Module 3 runs from Monday, Feb 03, 2026 to Sunday, Feb 09, 2026.
Source: course_schedule.md#module-sequence (M03)
```

---

### Discussion Open/Close Dates

**Markdown:**
```markdown
- **Opens (display):** Monday, Feb 03, 2026
- **Opens (ISO):** 2026-02-03
- **Opens Time:** 12:00 AM
- **Closes (display):** Friday, Feb 07, 2026
- **Closes (ISO):** 2026-02-07
- **Closes Time:** 11:59 PM
- **Timezone:** America/Chicago
```

**JSON:**
```json
{
  "entity_id": "D03",
  "open_date_display": "Monday, Feb 03, 2026",
  "open_date_iso": "2026-02-03",
  "open_time": "12:00 AM",
  "close_date_display": "Friday, Feb 07, 2026",
  "close_date_iso": "2026-02-07",
  "close_time": "11:59 PM",
  "timezone": "America/Chicago"
}
```

---

## HANDLING UNKNOWNS AND TBD DATES

### When Due Date is Not Yet Announced

**Markdown:**
```markdown
- **Due Date (display):** TBD
- **Due Date (ISO):** null
- **Due Time:** null
```

**JSON:**
```json
{
  "entity_id": "A07",
  "due_date_display": "TBD",
  "due_date_iso": null,
  "due_time": null
}
```

**Agent Response:**
```
Assignment A07 due date: TBD (To Be Determined)
Source: course_schedule.md#assignment-calendar (A07)

This due date has not been announced yet. Please check Canvas for updates or ask the instructor.
```

**Rules:**
- Use `"TBD"` for `display_date`
- Use `null` (not empty string) for `iso_date` and time fields
- Agent MUST state "TBD (To Be Determined)" and NOT guess or invent a date

---

### When Only a Week or Month is Known

**Example:** "Due sometime in Week 5"

**Markdown:**
```markdown
- **Due Date (display):** Week of Feb 03, 2026 (specific date TBD)
- **Due Date (ISO):** null
- **Approximate ISO Range:** 2026-02-03 to 2026-02-09
```

**Agent Response:**
```
Assignment A05 is due during the week of Feb 03, 2026 (specific date and time TBD).
Source: course_schedule.md#assignment-calendar (A05)
```

**Rule:** Do NOT pick a specific date within the range. State the range and mark specific date as TBD.

---

## DATE RANGE FORMATTING

### Standard Range Format

**Pattern:** `{start_display} to {end_display}`

**Examples:**
- `Monday, Jan 20, 2026 to Friday, May 08, 2026` (term dates)
- `Monday, Feb 03, 2026 to Sunday, Feb 09, 2026` (module dates)

**JSON:**
```json
{
  "start_date_display": "Monday, Jan 20, 2026",
  "start_date_iso": "2026-01-20",
  "end_date_display": "Friday, May 08, 2026",
  "end_date_iso": "2026-05-08"
}
```

---

## CURRENT DATE AND TIME REFERENCES

### Referencing "Today" or "This Week"

**Agent behavior:**
- When user asks "What is due this week?", agent must calculate based on current date
- Agent should state the current date in responses for clarity

**Example:**
```
Today is Saturday, Jan 25, 2026.

Assignments due this week (Jan 20 - Jan 26):
- Assignment A02: Due Monday, Jan 20, 2026 at 11:59 PM CT (OVERDUE)
- Discussion D02: Closes Sunday, Jan 26, 2026 at 11:59 PM CT (DUE TOMORROW)

Source: course_schedule.md#assignment-calendar
```

**Note:** Agent must know or be told the current date to calculate relative deadlines.

---

## VALIDATION RULES

### Validation Checklist for Date/Time Fields

1. **display_date validation:**
   - Matches regex: `^(Monday|Tuesday|...|Sunday), (Jan|Feb|...|Dec) (0[1-9]|[12][0-9]|3[01]), (20\d{2})$`
   - Day of week matches actual day for given date
   - Day is valid for month/year

2. **iso_date validation:**
   - Matches regex: `^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$`
   - Valid ISO 8601 date
   - Day is valid for month/year

3. **Correspondence check:**
   - `display_date` and `iso_date` MUST refer to the same calendar date
   - Example: `"Monday, Feb 10, 2026"` and `"2026-02-10"` are correct
   - Example: `"Monday, Feb 10, 2026"` and `"2026-02-11"` is INVALID

4. **Time validation:**
   - Matches regex: `^(1[0-2]|[1-9]):[0-5][0-9] (AM|PM)$`
   - Hour is 1-12
   - Minutes are 00-59
   - AM/PM is uppercase

5. **TBD handling:**
   - If `display_date = "TBD"`, then `iso_date = null` (not empty string)
   - If `iso_date = null`, then `display_date = "TBD"` (must be consistent)

---

## SPECIAL CASES

### Case 1: Assignment Due at Start of Class

**Scenario:** Assignment due "at the beginning of class" on Monday, Feb 10, 2026, where class starts at 2:00 PM.

**Encoding:**
```markdown
- **Due Date (display):** Monday, Feb 10, 2026
- **Due Date (ISO):** 2026-02-10
- **Due Time:** 2:00 PM (start of class)
```

**Agent Response:**
```
Assignment A04 is due Monday, Feb 10, 2026 at 2:00 PM CT (start of class).
Source: course_schedule.md#assignment-calendar (A04)
```

---

### Case 2: Reading Due "Before" a Specific Class

**Scenario:** Reading assigned "before class on Wednesday, Feb 12."

**Encoding:**
```markdown
- **Due Date (display):** Wednesday, Feb 12, 2026
- **Due Date (ISO):** 2026-02-12
- **Due Time:** Before 2:00 PM (before class)
```

**JSON (optional qualifier):**
```json
{
  "entity_id": "M04-R01",
  "due_date_display": "Wednesday, Feb 12, 2026",
  "due_date_iso": "2026-02-12",
  "due_time": "Before 2:00 PM",
  "due_qualifier": "before_class"
}
```

**Agent Response:**
```
Reading M04-R01 is due before class on Wednesday, Feb 12, 2026 (class starts at 2:00 PM CT).
Source: course_schedule.md#reading-schedule (M04-R01)
```

---

### Case 3: Multi-Day Event (e.g., Conference, Workshop)

**Scenario:** Attendance required at a workshop spanning Feb 15-16, 2026.

**Encoding:**
```markdown
- **Event:** Industry Workshop (required attendance)
- **Start Date (display):** Saturday, Feb 15, 2026
- **Start Date (ISO):** 2026-02-15
- **End Date (display):** Sunday, Feb 16, 2026
- **End Date (ISO):** 2026-02-16
- **Time:** 9:00 AM to 5:00 PM each day
```

**Agent Response:**
```
Industry Workshop is scheduled for Saturday, Feb 15, 2026 to Sunday, Feb 16, 2026, 9:00 AM to 5:00 PM CT each day (required attendance).
Source: course_schedule.md#special-events
```

---

## DATE ARITHMETIC AND PACING

### Calculating Days Until Deadline

**Agent behavior:**
- When user asks "How many days until Assignment A03 is due?", agent should calculate based on current date and due date.

**Example:**
```
Current date: Saturday, Jan 25, 2026
Assignment A03 due date: Monday, Feb 10, 2026

Days until due: 16 days

Source: course_schedule.md#assignment-calendar (A03)
```

---

### Identifying Overdue Assignments

**Agent behavior:**
- Compare current date to `due_date_iso`
- If current date > due date → assignment is overdue

**Example:**
```
Current date: Saturday, Jan 25, 2026

Overdue assignments:
- Assignment A01: Was due Monday, Jan 13, 2026 at 11:59 PM CT (12 days overdue)
- Discussion D01: Was due Sunday, Jan 19, 2026 at 11:59 PM CT (6 days overdue)

Source: course_schedule.md#assignment-calendar
```

---

## SUMMARY TABLE

| Field Type | Format | Example | Required? | Use Case |
|------------|--------|---------|-----------|----------|
| `display_date` | `DayOfWeek, Mon DD, YYYY` | `Monday, Feb 10, 2026` | Yes (or "TBD") | Human-readable output |
| `iso_date` | `YYYY-MM-DD` | `2026-02-10` | Yes (or `null`) | Machine processing, sorting |
| `due_time` | `h:mm AM` or `h:mm PM` | `11:59 PM` | Conditional | Time-specific deadlines |
| `timezone` | `America/Chicago` or `CT` | `America/Chicago` | Recommended | Clarity on timezone |
| `last_updated` | `YYYY-MM-DD` | `2026-01-25` | Yes (metadata) | File update tracking |

---

## ENFORCEMENT

**All Grounded Knowledge Files, INDEX entries, and agent responses MUST comply with this standard.**

**Validation script MUST check:**
1. Dual date fields present and correctly formatted
2. Correspondence between `display_date` and `iso_date`
3. Time format compliance (12-hour, AM/PM)
4. TBD handling (null for `iso_date`, "TBD" for `display_date`)

**No exceptions.**

---

**END OF DOCUMENT**