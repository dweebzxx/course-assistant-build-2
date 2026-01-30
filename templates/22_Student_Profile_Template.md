# Student Profile Template

**Filename Pattern:** `{course_id}.student_profile.md`  
**Regex:** `^[A-Z0-9\-]+\.student_profile\.md$`  
**Authority Tier:** 3 (Authoritative for student context)  
**Example Filename:** `MGMT-5001-SEC01-2026-SP.student_profile.md`

**Purpose:** Captures minimal student-specific context required for personalized agent responses. This file is designed to be portable across courses with minimal editing.

**Constraint:** This file is authoritative for student context ONLY. It may NOT contradict course requirements defined in course_core.md or course_schedule.md.

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `{COURSE_ID}` |
| **term_id** | `{YYYY}-{TT}` |
| **doc_type** | `student_profile` |
| **last_updated** | `{YYYY-MM-DD}` |
| **timezone** | `America/Chicago` |
| **student_name** | `Josh` |

**Change Log (optional):**
- {YYYY-MM-DD}: {Description of change}

---

## Student Identification
<!-- anchor: #student-identification -->

| Field | Value |
|-------|-------|
| **First Name** | Josh |
| **Preferred Name** | {Josh or preferred name} |
| **Program** | {e.g., MBA, MS Finance, Undergraduate Marketing} |
| **Year** | {e.g., First year, Second year, Senior} |
| **Timezone** | {e.g., America/Chicago (CT)} |

---

## Writing Style Profile
<!-- anchor: #writing-style-profile -->

{Brief summary of Josh's writing characteristics to help the agent provide appropriately styled assistance.}

| Attribute | Description |
|-----------|-------------|
| **Voice** | {e.g., "Professional but accessible; avoids jargon when possible"} |
| **Structure** | {e.g., "Strong opening statements; uses headers and bullets for organization"} |
| **Strengths** | {e.g., "Clear argumentation, good use of evidence"} |
| **Development Areas** | {e.g., "Sometimes too verbose; could be more concise"} |
| **Citation Style** | {APA / MLA / Chicago / Course-specific} |

---

## Group Project Assignment
<!-- anchor: #group-project-assignment -->

{Josh's group project assignment details, if applicable. This section only applies when the course has a group project (see course_core.md#group-project-context).}

| Field | Value |
|-------|-------|
| **Assigned to Group Project** | Yes / No |
| **Project ID** | {PROJ-FINAL or GP01, or N/A} |
| **Team Name** | {Team name if assigned, or N/A} |
| **Josh's Role** | {e.g., Data Analysis Lead, or N/A} |

### Team Structure (if applicable)

| Role | Member ID | 
|------|-----------|
| {Team Lead} | {Member 01 / Josh} |
| {Research Lead} | {Member 02} |
| {Analysis Lead} | {Member 03} |
| {Writing Lead} | {Member 04} |

### Milestone Ownership (if applicable)

| Milestone ID | Josh's Deliverables | Status |
|--------------|---------------------|--------|
| MS01 | {e.g., "Draft team charter"} | {Not started / In progress / Complete} |
| MS02 | {Josh's specific deliverables} | {Status} |

{Note: Milestone dates and deadlines are in course_schedule.md. Group project definition is in course_core.md.}

---

## Known Challenges
<!-- anchor: #known-challenges -->

{Areas where Josh anticipates needing additional support or practice (3-5 items max).}

- {Challenge 1, e.g., "Statistical analysis - need extra practice with regression"}
- {Challenge 2, e.g., "Time management during group projects"}
- {Challenge 3, e.g., "Public speaking for presentations"}

---

## Index References
<!-- anchor: #index-references -->

This file contains the following sections indexed for retrieval:

| Section Anchor | Section Title | Entity IDs |
|----------------|---------------|------------|
| #metadata | Metadata | — |
| #student-identification | Student Identification | — |
| #writing-style-profile | Writing Style Profile | — |
| #group-project-assignment | Group Project Assignment | {PROJECT_ID} |
| #known-challenges | Known Challenges | — |
| #index-references | Index References | — |

---

## Template Validation Checklist

Before finalizing student_profile.md, verify:

- [ ] course_id matches course_core.md and course_schedule.md exactly
- [ ] term_id matches other Grounded Knowledge Files
- [ ] student_name is "Josh" (per system scope)
- [ ] All section headers have corresponding HTML comment anchors
- [ ] No personal names appear for team members (use Member 01, Member 02, etc.)
- [ ] No content contradicts course_core.md policies or course_schedule.md dates
- [ ] Group project assignment aligns with course_core.md#group-project-context

---

**END OF STUDENT PROFILE TEMPLATE**
