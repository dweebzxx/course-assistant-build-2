# Acceptance Test Suite

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Acceptance test specification  
**Date:** 2026-01-25  
**Phase:** 8  
**Status:** Production-ready

---

## PURPOSE

This document provides exactly 10 acceptance test queries to validate the operational readiness of a Course Assistant AI agent build. Tests cover course facts, pacing, and assignment questions. Each test includes expected behavior, required citation format, and pass/fail criteria.

Run these tests after completing the setup sequence (50_Setup_Prompt_Sequence.md).

---

## TEST SUITE

### Test 1: Course Policy Retrieval

**Category:** Course Facts

**Query:**
```
What is the course policy on academic integrity?
```

**Expected Behavior:**
1. Agent consults INDEX to locate policy section
2. Agent retrieves content from `course_core.md#academic-integrity` (or equivalent section)
3. Agent extracts policy exactly as stated (no paraphrasing unless very long)
4. Agent cites source using format: `Source: course_core.md#section-anchor`
5. If policy not found, agent states "Not found in provided materials" and suggests where to find it

**Required Citation Format:**
```
Source: course_core.md#academic-integrity
```
(Or equivalent section anchor)

**Pass Criteria:**
- ✅ Agent retrieves correct policy text (if present in course_core.md)
- ✅ Agent cites source using exact format: `filename#section-anchor`
- ✅ Agent does NOT synthesize or invent policy
- ✅ If missing, agent states "Not found in provided materials"

**Fail Criteria:**
- ❌ Agent invents or synthesizes policy
- ❌ Agent fails to cite source
- ❌ Agent cites incorrect source (e.g., course_schedule.md)
- ❌ Agent uses incorrect citation format

---

### Test 2: Grading Component Weight

**Category:** Course Facts

**Query:**
```
How much is the final exam worth in the overall grade?
```

**Expected Behavior:**
1. Agent consults INDEX to locate grading policy section
2. Agent retrieves content from `course_core.md#grading-policy`
3. Agent extracts exact percentage or points for final exam
4. Agent cites source using format: `Source: course_core.md#grading-policy`
5. If not found, agent states "Not found in provided materials"

**Required Citation Format:**
```
Source: course_core.md#grading-policy
```

**Pass Criteria:**
- ✅ Agent retrieves correct percentage/points for final exam
- ✅ Agent cites source correctly
- ✅ Agent does NOT guess or estimate
- ✅ If missing, agent states "Not found in provided materials"

**Fail Criteria:**
- ❌ Agent invents or guesses percentage
- ❌ Agent fails to cite source
- ❌ Agent cites incorrect section

---

### Test 3: Assignment Due Date and Time

**Category:** Date/Deadline Query

**Query:**
```
When is Assignment A03 due?
```

**Expected Behavior:**
1. Agent consults INDEX to locate assignment A03
2. Agent retrieves `due_date_display`, `due_date_iso`, and `due_time` from `course_schedule.md#assignment-calendar`
3. Agent formats response as: `DayOfWeek, Mon DD, YYYY at h:mm AM/PM CT`
4. Agent cites source using format: `Source: course_schedule.md#assignment-calendar (A03)`
5. If not found or TBD, agent states appropriately

**Required Citation Format:**
```
Source: course_schedule.md#assignment-calendar (A03)
```

**Pass Criteria:**
- ✅ Agent provides due date in required format: `DayOfWeek, Mon DD, YYYY at h:mm AM/PM CT`
- ✅ Agent includes time with AM/PM and timezone
- ✅ Agent cites using format: `filename#section-anchor (entity_id)`
- ✅ If TBD, agent states "TBD (To Be Determined)" and cites source

**Fail Criteria:**
- ❌ Agent uses incorrect date format
- ❌ Agent omits time or timezone
- ❌ Agent fails to cite source with entity_id
- ❌ Agent invents date if not present

---

### Test 4: Module Date Range

**Category:** Date/Deadline Query

**Query:**
```
What are the dates for Module 3?
```

**Expected Behavior:**
1. Agent consults INDEX to locate module M03
2. Agent retrieves `start_date_display`, `start_date_iso`, `end_date_display`, `end_date_iso` from `course_schedule.md#module-sequence`
3. Agent formats response as date range: `DayOfWeek, Mon DD, YYYY to DayOfWeek, Mon DD, YYYY`
4. Agent cites source using format: `Source: course_schedule.md#module-sequence (M03)`

**Required Citation Format:**
```
Source: course_schedule.md#module-sequence (M03)
```

**Pass Criteria:**
- ✅ Agent provides date range in required format
- ✅ Agent cites using format: `filename#section-anchor (entity_id)`
- ✅ If module not found, agent states "Not found in provided materials"

**Fail Criteria:**
- ❌ Agent uses incorrect date format
- ❌ Agent omits start or end date
- ❌ Agent fails to cite source
- ❌ Agent invents dates

---

### Test 5: Pacing Check (This Week)

**Category:** Pacing and Planning

**Query:**
```
What assignments are due this week?
```
(Assume current date is provided by system or user states: "Today is Monday, Feb 03, 2026")

**Expected Behavior:**
1. Agent determines current date (Feb 03, 2026)
2. Agent defines "this week" as current_date to current_date + 7 days
3. Agent consults INDEX to retrieve all assignments with `due_date_iso` in range
4. Agent lists assignments with due dates and times
5. Agent cites source for each assignment: `Source: course_schedule.md#assignment-calendar (entity_id)`
6. Agent discloses assumption: "Assuming today is Monday, Feb 03, 2026"

**Required Citation Format:**
```
Source: course_schedule.md#assignment-calendar (A03)
Source: course_schedule.md#discussion-schedule (D03)
```
(One citation per entity)

**Pass Criteria:**
- ✅ Agent correctly filters assignments by date range (this week)
- ✅ Agent lists all assignments due in range with due dates/times
- ✅ Agent cites each assignment individually
- ✅ Agent discloses date assumption

**Fail Criteria:**
- ❌ Agent omits assignments due this week
- ❌ Agent includes assignments outside date range
- ❌ Agent fails to cite sources
- ❌ Agent does not disclose date assumption

---

### Test 6: Overdue Check

**Category:** Pacing and Planning

**Query:**
```
Do I have any overdue assignments?
```
(Assume current date: "Today is Monday, Feb 10, 2026")

**Expected Behavior:**
1. Agent determines current date (Feb 10, 2026)
2. Agent consults INDEX to retrieve all assignments with `due_date_iso < current_date`
3. Agent checks `student_profile.md#progress-tracking` to see if assignment is marked complete
4. Agent lists any overdue assignments that are NOT marked complete
5. Agent cites source for each
6. If progress tracking not maintained, agent states limitation
7. Agent discloses assumption about current date

**Required Citation Format:**
```
Source: course_schedule.md#assignment-calendar (A02)
Source: student_profile.md#progress-tracking
```

**Pass Criteria:**
- ✅ Agent correctly identifies overdue assignments (due_date_iso < current_date)
- ✅ Agent checks progress tracking if maintained
- ✅ Agent cites both schedule and progress tracking sources
- ✅ If progress tracking not maintained, agent states limitation clearly
- ✅ Agent discloses date assumption

**Fail Criteria:**
- ❌ Agent fails to check progress tracking
- ❌ Agent incorrectly calculates overdue status
- ❌ Agent fails to cite sources
- ❌ Agent does not disclose limitations or assumptions

---

### Test 7: Assignment Requirements Retrieval

**Category:** Assignment Execution Support

**Query:**
```
What are the requirements for Assignment A05?
```

**Expected Behavior:**
1. Agent consults INDEX to locate assignment A05
2. Agent retrieves basic info from `course_schedule.md#assignment-calendar (A05)`: title, due date, points
3. Agent checks INDEX for `related_sections` pointing to module files (e.g., `M05/Assignment_A05_Instructions.pdf`)
4. Agent retrieves detailed requirements from module instruction file (if available)
5. Agent synthesizes response:
   - Due date from course_schedule.md (AUTHORITATIVE)
   - Detailed requirements from module file (SUPPORTIVE)
   - Cites BOTH sources
6. If detailed requirements not found, agent states "Not found in provided materials" and suggests checking module upload

**Required Citation Format:**
```
Sources:
- course_schedule.md#assignment-calendar (A05) [dates and basic info]
- M05/Assignment_A05_Instructions.pdf [detailed requirements]
```

**Pass Criteria:**
- ✅ Agent retrieves due date from course_schedule.md
- ✅ Agent checks for detailed requirements in module files
- ✅ Agent cites BOTH sources (schedule + module file)
- ✅ Agent marks course_schedule.md as authoritative for dates
- ✅ If detailed requirements missing, agent states clearly and suggests module upload check

**Fail Criteria:**
- ❌ Agent only checks one source
- ❌ Agent fails to cite both sources
- ❌ Agent invents requirements
- ❌ Agent does not differentiate authoritative vs supportive sources

---

### Test 8: Conflict Detection (Date Contradiction)

**Category:** Conflict Resolution

**Query:**
```
I noticed Assignment A03 instructions say it's due February 12, but the course schedule says February 10. Which is correct?
```

**Expected Behavior:**
1. Agent recognizes this as a conflict scenario
2. Agent flags conflict explicitly: "CONFLICT DETECTED:"
3. Agent reports both sources and their values
4. Agent states course_schedule.md is authoritative (Tier 1 for dates)
5. Agent provides authoritative answer (Feb 10)
6. Agent suggests user verify with instructor if concerned

**Required Response Pattern:**
```
CONFLICT DETECTED:

course_schedule.md#assignment-calendar (A03) states: Due Monday, Feb 10, 2026 at 11:59 PM
M03/Assignment_A03_Instructions.pdf states: Due February 12, 2026

The Grounded Knowledge File (course_schedule.md) is the authoritative source for dates.

Assignment A03 is due: Monday, Feb 10, 2026 at 11:59 PM CT

Source: course_schedule.md#assignment-calendar (A03) [AUTHORITATIVE]

Note: The module instruction file lists a different date (February 12). If this is a course update, please verify with the instructor or update course_schedule.md.
```

**Pass Criteria:**
- ✅ Agent flags conflict explicitly
- ✅ Agent reports both sources and values
- ✅ Agent states which source is authoritative
- ✅ Agent provides authoritative answer
- ✅ Agent suggests user action (verify with instructor)

**Fail Criteria:**
- ❌ Agent does not flag conflict
- ❌ Agent does not explain authority hierarchy
- ❌ Agent provides wrong authoritative source
- ❌ Agent synthesizes a "compromise" date

---

### Test 9: Module Content Summary

**Category:** Module Navigation

**Query:**
```
What is in Module 3?
```

**Expected Behavior:**
1. Agent consults INDEX to locate module M03
2. Agent retrieves module overview from `course_schedule.md#module-sequence (M03)`: dates, title, topics
3. Agent checks if module files are uploaded (checks INDEX `working_memory_files` section)
4. If module uploaded:
   - Agent retrieves learning objectives and file inventory from `M03/M03.module_manifest.md`
   - Agent lists module materials
5. If module not uploaded:
   - Agent states module files not yet uploaded
   - Agent provides what's in schedule (dates, title, topics)
   - Agent explains how to upload module
6. Agent cites all sources

**Required Citation Format:**
```
Source: course_schedule.md#module-sequence (M03)
Source: M03/M03.module_manifest.md#overview
Source: M03/M03.module_manifest.md#file-inventory
```

**Pass Criteria:**
- ✅ Agent retrieves module dates and title from course_schedule.md
- ✅ Agent checks for uploaded module files
- ✅ If uploaded, agent retrieves learning objectives and file inventory
- ✅ If not uploaded, agent states limitation and explains upload process
- ✅ Agent cites all sources used

**Fail Criteria:**
- ❌ Agent only checks one source
- ❌ Agent invents module content
- ❌ Agent fails to check if module uploaded
- ❌ Agent does not cite sources

---

### Test 10: Student Context Retrieval (Group Project Role)

**Category:** Student-Specific Information

**Query:**
```
What is my role in the group project?
```

**Expected Behavior:**
1. Agent consults `student_profile.md#group-project-context`
2. Agent retrieves student role, responsibilities, and team structure
3. Agent uses anonymized team member labels (Member 01, Member 02, etc.)
4. Agent cross-references with `course_schedule.md#milestone-timeline` to identify upcoming milestones student owns
5. Agent cites both sources
6. Agent does NOT include personal names of other team members

**Required Citation Format:**
```
Source: student_profile.md#group-project-context
Source: course_schedule.md#milestone-timeline
```

**Pass Criteria:**
- ✅ Agent retrieves student role from student_profile.md
- ✅ Agent lists responsibilities clearly
- ✅ Agent uses anonymized team structure (Member 01, etc.)
- ✅ Agent identifies upcoming milestones student owns
- ✅ Agent cites both sources
- ✅ Agent does NOT include personal names

**Fail Criteria:**
- ❌ Agent includes personal names of other team members
- ❌ Agent fails to cite student_profile.md
- ❌ Agent does not cross-reference milestones
- ❌ Agent invents role or responsibilities

---

## TEST SUMMARY REPORT

After running all 10 tests, complete this summary:

| Test # | Test Name | Category | Status | Notes |
|--------|-----------|----------|--------|-------|
| 1 | Course Policy Retrieval | Course Facts | ☐ Pass ☐ Fail | |
| 2 | Grading Component Weight | Course Facts | ☐ Pass ☐ Fail | |
| 3 | Assignment Due Date | Date/Deadline | ☐ Pass ☐ Fail | |
| 4 | Module Date Range | Date/Deadline | ☐ Pass ☐ Fail | |
| 5 | Pacing Check (This Week) | Pacing | ☐ Pass ☐ Fail | |
| 6 | Overdue Check | Pacing | ☐ Pass ☐ Fail | |
| 7 | Assignment Requirements | Assignment Support | ☐ Pass ☐ Fail | |
| 8 | Conflict Detection | Conflict Resolution | ☐ Pass ☐ Fail | |
| 9 | Module Content Summary | Module Navigation | ☐ Pass ☐ Fail | |
| 10 | Group Project Role | Student Context | ☐ Pass ☐ Fail | |

**Total Passed:** ___ / 10

**Acceptance Threshold:** 10 / 10 (100% pass required for production readiness)

---

## REMEDIATION ACTIONS

If any test fails:

1. **Identify root cause:**
   - File missing or malformed?
   - INDEX not updated?
   - Agent instructions not correctly implemented?
   - Schema validation failure?

2. **Apply fix:**
   - Re-upload corrected file
   - Regenerate INDEX
   - Re-validate schemas
   - Update agent instructions

3. **Re-run failed test(s)**

4. **Re-run full test suite to confirm no regressions**

---

## PRODUCTION READINESS CERTIFICATION

**Agent is production-ready when:**
- ✅ All 10 acceptance tests pass
- ✅ All setup prompts completed successfully
- ✅ All schema validations pass
- ✅ INDEX is current and validated

**Certification Date:** __________

**Certified By:** __________

---

**END OF ACCEPTANCE TEST SUITE**