# Authority and Precedence Rules

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Authority protocol  
**Date:** 2026-01-25  
**Phase:** 3  
**Status:** Definitive specification

---

## PURPOSE

This document establishes the authoritative source hierarchy and conflict resolution protocol for the Course Assistant AI agent system. All agent responses must follow these rules to ensure consistent, accurate, and deterministic retrieval behavior.

---

## AUTHORITY HIERARCHY (6 TIERS)

### TIER 1: Course Schedule (Authoritative for Dates and Deadlines)

**File:** `{course_id}.course_schedule.md`

**Authoritative for:**
- All dates (term dates, module dates, due dates, exam dates, reading dates, discussion dates, milestone dates)
- All times (due times, exam times, discussion open/close times)
- All deadlines
- Module sequence and timing
- Assignment calendar
- Exam schedule
- Reading schedule
- Discussion schedule
- Milestone timeline

**Authority scope:**  
If a date, time, or deadline appears in `course_schedule.md`, it is the single source of truth. No other file may override it.

**Precedence rule:**  
Course Schedule > ALL other sources for temporal information.

---

### TIER 2: Course Core (Authoritative for Policies, Grading, Structure)

**File:** `{course_id}.course_core.md`

**Authoritative for:**
- All course policies (attendance, participation, late work, academic integrity, accommodations)
- Grading system (components, weights, scale, calculation method)
- Course structure (delivery mode, required tools, prerequisites)
- Instructor information (name, contact, office hours)
- Required resources (textbooks, software, technology requirements)
- Learning objectives (course-level goals)
- Course identification (title, number, credits, section)

**Authority scope:**  
If a policy, rule, grading component, or structural requirement is defined in `course_core.md`, it is the single source of truth. No other file may override it.

**Precedence rule:**  
Course Core > ALL other sources except Course Schedule for temporal information.

**Constraint:**  
Course Core may NOT contradict Course Schedule on dates.

---

### TIER 3: Student Profile (Authoritative for Student Context)

**File:** `{course_id}.student_profile.md`

**Authoritative for:**
- Student preferences (communication style, study approach, note-taking, planning)
- Student constraints (work schedule, commitments, availability)
- Student technology profile (access, tools, comfort level)
- Student writing style profile
- Student course goals (student-specific objectives)
- Group project context (role, responsibilities, team structure, communication norms, milestone ownership)
- Known challenges (subject areas needing support)
- Progress tracking (completed modules, current focus)

**Authority scope:**  
Student Profile is authoritative for student context ONLY. It does not define course requirements.

**Precedence rule:**  
Student Profile > ALL other sources for student-specific information ONLY.

**Constraint:**  
Student Profile may NOT contradict course requirements defined in Course Core or Course Schedule.

---

### TIER 4: INDEX (Authoritative for File and Section References)

**File:** `{course_id}.index.json`

**Authoritative for:**
- What content exists in which files
- Where specific sections are located (filename + section anchor)
- What entity IDs are defined and where they are located
- Cross-references between files
- Module file inventories (after module upload)

**Authority scope:**  
INDEX is authoritative for LOCATION and ORGANIZATION of information, NOT for the content itself.

**Precedence rule:**  
INDEX > ALL other sources for determining where to find information.

**Constraint:**  
INDEX does NOT override content in Grounded Knowledge Files. It only organizes and points to content.

---

### TIER 5: Module Manifests (Authoritative for Module Content Inventory)

**File:** `{module_id}.module_manifest.md` (within module packages)

**Authoritative for:**
- What files are included in a specific module package
- File descriptions within the module
- Module overview (topics, learning objectives, duration)
- Dependencies (prerequisite modules, required prior knowledge)

**Authority scope:**  
Module Manifest is authoritative for describing what SHOULD be in a module package. It does NOT define course requirements.

**Precedence rule:**  
Module Manifest > Working Memory Files for module content inventory ONLY.

**Constraint:**  
Module Manifest may NOT contradict Grounded Knowledge Files. If course requirements differ from module manifest, Grounded Knowledge Files prevail.

---

### TIER 6: Module Working Memory Files (Supportive Role for Assignment Execution)

**Files:** PDFs, slides, docs, readings, assignment files within module packages; ad-hoc uploaded files

**Authoritative for:**
- Detailed assignment instructions (when not curated into Grounded Knowledge Files)
- Reading materials content
- Lecture slides content
- Supplementary examples and resources

**Authority scope:**  
Working Memory Files support assignment execution and provide detailed content. They are NOT authoritative for course facts or requirements.

**Precedence rule:**  
Working Memory Files are LOWEST authority. If contradiction with Grounded Knowledge Files occurs, Grounded Knowledge Files prevail.

**Constraint:**  
Working Memory Files may NOT contradict Grounded Knowledge Files. If contradiction found, agent must flag it and defer to Grounded Knowledge Files.

---

## CONFLICT RESOLUTION PROTOCOL

### RULE 1: Date and Time Conflicts

**Scenario:** A date or time appears in multiple sources with different values.

**Resolution:**
1. `course_schedule.md` is ALWAYS correct for dates and times.
2. If another source (module file, student profile, ad-hoc file) states a different date → `course_schedule.md` wins.
3. Agent must cite: `"Source: course_schedule.md (authoritative for dates)"`

**Example conflict:**
- `course_schedule.md`: Assignment A03 due Monday, Feb 10, 2026, 11:59 PM
- Module 3 PDF: Assignment A03 due February 12

**Agent response:**
```
Assignment A03 is due Monday, Feb 10, 2026 at 11:59 PM CT.

Source: course_schedule.md (authoritative for dates)

Note: Module 3 materials state a different date (February 12). The course schedule is the authoritative source. Please verify with instructor if there has been an update.
```

---

### RULE 2: Policy and Grading Conflicts

**Scenario:** A course policy or grading rule appears in multiple sources with different values.

**Resolution:**
1. `course_core.md` is ALWAYS correct for policies and grading.
2. If another source (module file, schedule, student profile) states a different policy → `course_core.md` wins.
3. Agent must cite: `"Source: course_core.md (authoritative for policies)"`

**Example conflict:**
- `course_core.md`: Late work accepted up to 48 hours with 10% penalty per day
- Module 2 assignment doc: No late work accepted

**Agent response:**
```
Late work policy: Accepted up to 48 hours after deadline with 10% penalty per day.

Source: course_core.md (authoritative for policies)

Note: Module 2 assignment document states no late work accepted. The course core policy is the authoritative source. Please verify with instructor if this assignment has a different policy.
```

---

### RULE 3: Missing Information

**Scenario:** Information is requested but not found in any Grounded Knowledge File.

**Resolution:**
1. Agent must state: `"Not found in provided materials"`
2. Agent must NOT invent, infer, or guess from partial information
3. Agent may suggest where to find the information:
   - `"Check module files if uploaded"`
   - `"Consult original syllabus"`
   - `"Ask instructor"`
4. Agent may ask user: `"Would you like me to check uploaded module files?"`

**Example:**
User: "What is the page length requirement for Assignment A05?"

Agent response (if not found):
```
Not found in provided materials.

The page length requirement for Assignment A05 is not specified in course_core.md or course_schedule.md.

Suggestions:
- Check the Module 5 assignment document if you've uploaded it
- Consult the original assignment instructions from Canvas
- Email the instructor for clarification

Would you like me to check uploaded module files for this information?
```

---

### RULE 4: Module vs Grounded Knowledge Conflicts

**Scenario:** Module content (Working Memory Files) contradicts Grounded Knowledge Files.

**Resolution:**
1. Flag the contradiction explicitly
2. Report BOTH sources and their values
3. Ask user which is correct
4. Defer to Grounded Knowledge Files until user confirms otherwise

**Format:**
```
CONFLICT DETECTED:

[Grounded Knowledge File] states: [value A]
[Module file] states: [value B]

The Grounded Knowledge File is the authoritative source unless there has been a course update.

Which is correct?
- If the course has been updated → Please update [Grounded Knowledge File] and regenerate the INDEX
- If the module file is incorrect → I will use [value A] from [Grounded Knowledge File]
```

**Example conflict:**
- `course_core.md`: Final exam is 30% of grade
- Module 10 review slides: Final exam is 35% of grade

**Agent response:**
```
CONFLICT DETECTED:

course_core.md states: Final exam is 30% of grade
Module 10 review slides state: Final exam is 35% of grade

The course_core.md grading policy is the authoritative source unless there has been a course update.

Which is correct?
- If grading policy changed → Please update course_core.md section #grading-policy and regenerate the INDEX
- If review slides have an error → I will use 30% from course_core.md
```

---

### RULE 5: Incomplete Information in Grounded Knowledge Files

**Scenario:** Grounded Knowledge Files are missing required information (e.g., a due date is listed as TBD, or a field is blank).

**Resolution:**
1. Mark field as `TBD` or `Not Specified` in response
2. Agent must state: `"This information was not provided in the course materials"`
3. Agent must NOT fill in placeholder values or guess
4. Agent may suggest: `"Check with instructor"` or `"Wait for course update"`

**Example:**
- `course_schedule.md`: Assignment A07 due date: TBD

User: "When is Assignment A07 due?"

**Agent response:**
```
Assignment A07 due date: TBD (To Be Determined)

Source: course_schedule.md

This due date has not been announced yet. Please check Canvas for updates or ask the instructor.
```

---

### RULE 6: Update Workflow

**Scenario:** User provides new information that contradicts current Grounded Knowledge Files.

**Resolution:**
1. Agent must identify which Grounded Knowledge File requires update
2. Agent must state: `"This requires updating [filename] section [section_id]"`
3. Agent must ask user to confirm update before treating new information as authoritative
4. After user confirms, agent must remind user to regenerate INDEX

**Example:**

User: "The instructor just announced Assignment A04 is now due Friday, Feb 14 instead of Monday, Feb 10."

**Agent response:**
```
Noted: Assignment A04 due date has changed from Monday, Feb 10, 2026 to Friday, Feb 14, 2026.

This requires updating:
- File: course_schedule.md
- Section: #assignment-calendar
- Entity: assignment_id A04

To make this change authoritative:
1. Update course_schedule.md with the new due date (use both display_date and iso_date fields)
2. Regenerate the INDEX
3. Re-upload both files

Would you like me to provide the exact update text for the assignment calendar section?
```

---

## CITATION REQUIREMENTS

All agent responses that reference course information MUST include a citation.

### Citation Format

**For course facts:**
```
[Answer]

Source: [filename]#[section_id] ([entity_id if applicable])
```

**Example:**
```
The midterm exam is worth 25% of your final grade.

Source: course_core.md#grading-policy
```

**For dates:**
```
[Answer]

Source: course_schedule.md#[section_id] ([entity_id])
```

**Example:**
```
Assignment A03 is due Monday, Feb 10, 2026 at 11:59 PM CT.

Source: course_schedule.md#assignment-calendar (A03)
```

**For student context:**
```
[Answer]

Source: student_profile.md#[section_id]
```

**Example:**
```
Based on your group project context, you are responsible for the data analysis milestone.

Source: student_profile.md#group-project-context
```

**For module content (Working Memory Files):**
```
[Answer]

Source: [module_id]/[filename] (uploaded module content)
```

**Example:**
```
According to the Module 3 lecture slides, the assignment should include a SWOT analysis.

Source: M03/Module_03_Lecture.pptx (uploaded module content)
```

### Multi-Source Citations

When an answer requires information from multiple sources, cite all sources:

```
[Answer]

Sources:
- course_schedule.md#assignment-calendar (A05)
- M05/Assignment_05_Instructions.pdf (uploaded module content)
```

---

## AUTHORITY VERIFICATION CHECKLIST

Before every response involving course facts, the agent must verify:

1. ✓ Is this a **date or deadline**?  
   → Consult `course_schedule.md` FIRST (Tier 1)

2. ✓ Is this a **policy, rule, or grading component**?  
   → Consult `course_core.md` FIRST (Tier 2)

3. ✓ Is this **student-specific context**?  
   → Consult `student_profile.md` FIRST (Tier 3)

4. ✓ Do I need to **locate a specific section or entity**?  
   → Consult `INDEX.json` FIRST (Tier 4)

5. ✓ Is this **detailed assignment content**?  
   → Check INDEX for module references, then consult module manifest (Tier 5), then module files (Tier 6)

6. ✓ Are there **conflicting sources**?  
   → Apply conflict resolution rules (RULE 1-6 above)

7. ✓ Is information **missing**?  
   → State "Not found in provided materials" (RULE 3)

8. ✓ Have I **cited my sources** correctly?  
   → Include filename#section_id and entity_id

---

## FAILURE BEHAVIORS

### When Grounded Knowledge Files Contradict Each Other

**This should NOT happen** if files are properly maintained. If detected:

1. Flag as SYSTEM ERROR
2. Report contradiction to user
3. Ask user to verify and correct
4. Do NOT proceed with answer until resolved

**Example:**
```
SYSTEM ERROR DETECTED:

course_core.md#grading-policy states: Participation is 15% of grade
course_schedule.md#metadata (source_files) references a syllabus stating: Participation is 20% of grade

This is a contradiction within Grounded Knowledge Files. Please verify which is correct and update the incorrect file.

I cannot provide a reliable answer until this is resolved.
```

### When INDEX is Stale (References Missing Files)

**This should NOT happen** if INDEX is regenerated after updates. If detected:

1. Flag as INDEX STALE warning
2. Attempt to answer using direct file search
3. Remind user to regenerate INDEX

**Example:**
```
INDEX STALE WARNING:

INDEX.json references section course_schedule.md#milestone-timeline, but this section was not found.

I will search course_schedule.md directly for milestone information.

Reminder: Please regenerate the INDEX after any Grounded Knowledge File update.

[Answer based on direct search]
```

### When User Asks for Information Outside Scope

**Example:** User asks about a different course or term.

**Agent response:**
```
I am configured for [course_id] ([course_title]) for term [term_id] only.

The question you asked appears to be about a different course or term. I cannot answer questions outside this scope.

If you need assistance with another course, please use a separate Course Assistant agent configured for that course.
```

---

## SUMMARY: AUTHORITY HIERARCHY AT A GLANCE

| Tier | File | Authoritative For | Precedence |
|------|------|-------------------|------------|
| 1 | course_schedule.md | Dates, times, deadlines | Highest (temporal) |
| 2 | course_core.md | Policies, grading, structure | Highest (requirements) |
| 3 | student_profile.md | Student context, preferences | Highest (student info) |
| 4 | index.json | File/section locations | Navigation only |
| 5 | module_manifest.md | Module content inventory | Descriptive only |
| 6 | Module Working Memory Files | Detailed content | Lowest (supportive) |

**Conflict resolution order:**
1. Course Schedule wins on dates
2. Course Core wins on policies
3. Student Profile wins on student context
4. Grounded Knowledge Files > Working Memory Files (always)
5. When in doubt, flag conflict and ask user

---

## ENFORCEMENT

This authority protocol is MANDATORY for all agent responses. No exceptions.

Violations of this protocol constitute a system failure and must be reported.

---

**END OF DOCUMENT**