# Setup Prompt Sequence

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Setup protocol  
**Date:** 2026-01-25  
**Phase:** 8  
**Status:** Production-ready

---

## PURPOSE

This document provides a step-by-step setup sequence for initializing a new Course Assistant AI agent build. Follow these prompts in order after uploading the initial Grounded Knowledge Files (course_core.md, course_schedule.md, student_profile.md, and INDEX.json).

---

## SETUP SEQUENCE

### Prompt 1: Confirm Agent Identity and Scope

**Prompt:**
```
Please confirm your configured course and scope. What course, term, and student are you designed to support?
```

**Expected Behavior:**
- Agent must state course_id, term_id, and student name (Josh)
- Agent must confirm single-course, single-term, single-student scope
- Agent must refuse to answer questions outside this scope

**Pass Criteria:**
- ✅ Agent correctly identifies course_id from uploaded files
- ✅ Agent correctly identifies term_id from uploaded files
- ✅ Agent confirms student is Josh
- ✅ Agent states scope boundaries clearly

**Fail Criteria:**
- ❌ Agent states incorrect course_id or term_id
- ❌ Agent does not mention scope boundaries
- ❌ Agent does not identify student name

---

### Prompt 2: Verify Grounded Knowledge Files

**Prompt:**
```
Please confirm that you have access to all three required Grounded Knowledge Files. For each file, state:
1. Filename
2. Document type
3. Last updated date
4. Number of major sections you can access

Do NOT list the section contents, just confirm you can see the structure.
```

**Expected Behavior:**
- Agent lists all three files: course_core.md, course_schedule.md, student_profile.md
- Agent confirms doc_type for each
- Agent confirms last_updated date for each
- Agent confirms it can see section structure (counts major sections)

**Pass Criteria:**
- ✅ Agent identifies all 3 files by exact filename
- ✅ Agent states doc_type correctly for each
- ✅ Agent states last_updated date for each
- ✅ Agent provides section count for each file

**Fail Criteria:**
- ❌ Agent cannot locate one or more files
- ❌ Agent lists incorrect doc_type
- ❌ Agent cannot access file structure

---

### Prompt 3: Verify INDEX and Entity Counts

**Prompt:**
```
Please verify the course INDEX. Report:
1. Index filename
2. Index version
3. Last updated date
4. Total count of entities by type:
   - Modules
   - Assignments
   - Exams
   - Readings
   - Discussions
   - Milestones (if applicable)

Do NOT list individual entity details, just provide the counts.
```

**Expected Behavior:**
- Agent locates INDEX.json
- Agent states index metadata (version, last_updated)
- Agent provides entity counts by type
- Agent confirms INDEX is readable and parseable

**Pass Criteria:**
- ✅ Agent identifies INDEX.json by exact filename
- ✅ Agent states index_version and last_updated
- ✅ Agent provides accurate entity counts for all types present
- ✅ Agent confirms no parsing errors

**Fail Criteria:**
- ❌ Agent cannot locate INDEX.json
- ❌ Agent reports parsing errors
- ❌ Agent provides obviously incorrect counts (e.g., 0 modules when schedule shows modules)

---

### Prompt 4: Test Authority Hierarchy (Retrieval Calibration)

**Prompt:**
```
I want to test your understanding of the authority hierarchy. Please answer this question:

"If course_schedule.md states Assignment A01 is due Monday, Feb 10, 2026, but a module instruction file states it is due February 12, 2026, which date should you report as the authoritative due date? Explain your reasoning and cite the authority hierarchy."
```

**Expected Behavior:**
- Agent states course_schedule.md is authoritative (Tier 1 for dates)
- Agent explains conflict resolution protocol
- Agent cites the 6-tier authority hierarchy
- Agent states it would flag the conflict and defer to course_schedule.md

**Pass Criteria:**
- ✅ Agent correctly identifies course_schedule.md as Tier 1 authority for dates
- ✅ Agent states it would use Feb 10, 2026 (from course_schedule.md)
- ✅ Agent mentions conflict flagging protocol
- ✅ Agent cites authority hierarchy

**Fail Criteria:**
- ❌ Agent states incorrect authoritative source
- ❌ Agent does not mention conflict detection
- ❌ Agent does not cite authority hierarchy

---

### Prompt 5: Test Course Fact Retrieval and Citation

**Prompt:**
```
What is the late work policy for this course? Please cite your source using the required citation format.
```

**Expected Behavior:**
- Agent retrieves late work policy from course_core.md#late-work-policy (or equivalent section)
- Agent extracts policy exactly as stated (no synthesis)
- Agent cites source using format: `Source: course_core.md#section-anchor`
- If policy not found, agent states "Not found in provided materials"

**Pass Criteria:**
- ✅ Agent retrieves correct policy text (if present)
- ✅ Agent cites using exact format: `filename#section-anchor`
- ✅ If missing, agent states "Not found in provided materials"
- ✅ Agent does NOT invent or guess policy

**Fail Criteria:**
- ❌ Agent synthesizes or invents policy
- ❌ Agent fails to cite source
- ❌ Agent uses incorrect citation format
- ❌ Agent cites wrong source (e.g., course_schedule.md for a policy)

---

### Prompt 6: Test Date Retrieval and Formatting

**Prompt:**
```
When is Assignment A01 due? Include both the date and time, and cite your source.
```

**Expected Behavior:**
- Agent retrieves due_date_display, due_date_iso, and due_time from course_schedule.md
- Agent formats response as: `DayOfWeek, Mon DD, YYYY at h:mm AM/PM CT`
- Agent cites source using format: `Source: course_schedule.md#section-anchor (A01)`
- If assignment not found, agent states "Not found in provided materials"

**Pass Criteria:**
- ✅ Agent provides correct due date in required format (display_date)
- ✅ Agent includes time with AM/PM and timezone (CT)
- ✅ Agent cites using format: `filename#section-anchor (entity_id)`
- ✅ If missing, agent states "Not found in provided materials"

**Fail Criteria:**
- ❌ Agent uses incorrect date format
- ❌ Agent omits time or timezone
- ❌ Agent fails to cite source
- ❌ Agent invents due date if not present

---

### Prompt 7: Test Module Upload Workflow (If Module Not Yet Uploaded)

**Prompt:**
```
I am about to upload Module M01.... Please explain the steps I should follow to properly upload and verify the module so you can index it correctly.
```

**Expected Behavior:**
- Agent explains module upload protocol from 30_Module_Upload_and_Usage_Protocol.md
- Agent states required files (module_manifest.md at minimum)
- Agent explains folder or zip naming convention
- Agent explains verification workflow (upload → verify → index → confirm)
- Agent offers to verify module after upload

**Pass Criteria:**
- ✅ Agent explains upload options (folder or zip)
- ✅ Agent mentions module_manifest.md requirement
- ✅ Agent explains naming convention ({module_id}/ or {module_id}.zip)
- ✅ Agent describes verification and indexing steps
- ✅ Agent offers to help with verification

**Fail Criteria:**
- ❌ Agent does not explain upload protocol
- ❌ Agent does not mention module_manifest.md
- ❌ Agent does not describe verification workflow

---

## SETUP CONFIRMATION

After completing all 7 prompts, confirm:

- ✅ Agent correctly identifies course, term, and student
- ✅ Agent can access all 3 Grounded Knowledge Files
- ✅ Agent can parse and use INDEX.json
- ✅ Agent understands and enforces authority hierarchy
- ✅ Agent retrieves course facts correctly and cites sources
- ✅ Agent formats dates and times correctly
- ✅ Agent understands module upload workflow

**If all checks pass:** Agent is ready for operational use.

**If any check fails:** Review agent instructions, re-upload files, and repeat setup sequence.

---

## POST-SETUP OPERATIONAL CHECK

Once setup is complete, proceed to 51_Acceptance_Test_Suite.md to run operational acceptance tests covering course facts, pacing, and assignment execution support.

---

**END OF SETUP SEQUENCE**