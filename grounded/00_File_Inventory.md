# File Inventory
**Agent Build Scope**: Single course, single term, single student (Josh)  
**Inventory Date**: 2026-01-25  
**Total Attachments Analyzed**: 11 files

---

## Target Course Packet

Based on filename analysis and content completeness, the **Target Course Packet** is:

**Course ID**: `CARLSON-SCHOOL-2025-FA`  
**Term ID**: `2025-FA`  
**Evidence**: Most complete course set with syllabus, detailed schedule, and full module tree structure.

| Filename | Type | Inferred Purpose | Subsystem | Status |
|----------|------|------------------|-----------|--------|
| Carlson-School-2025-FA.tree.ALL.txt | TXT | Complete module file tree with paths and sizes | Module/Working Memory | **Target - Authoritative** |

---

## Illustrative Examples (Other Courses)

These materials demonstrate structure patterns and inform template design but are NOT course facts for the agent build.

### MGMT-8001-2024-SP (Spring 2024)
| Filename | Type | Inferred Purpose | Subsystem | Status |
|----------|------|------------------|-----------|--------|
| MGMT-8001-2024-SP.course_core.md | MD | Course core file example | Grounded Knowledge | **Illustrative** |
| MGMT-8001-2024-SP.student_profile.md | MD | Student profile file example | Grounded Knowledge | **Illustrative** |
| MGMT-8001-2024-SP.syllabus.pdf | PDF | Original syllabus document | Source Material | **Illustrative** |

### IDSC-4444-2024-FA (Fall 2024)
| Filename | Type | Inferred Purpose | Subsystem | Status |
|----------|------|------------------|-----------|--------|
| IDSC-4444-2024-FA.course_core.md | MD | Course core file example | Grounded Knowledge | **Illustrative** |
| IDSC-4444-2024-FA.student_profile.md | MD | Student profile file example | Grounded Knowledge | **Illustrative** |
| IDSC-4444-2024-FA.syllabus.pdf | PDF | Original syllabus document | Source Material | **Illustrative** |

### OPIM-5771-2025-SP (Spring 2025)
| Filename | Type | Inferred Purpose | Subsystem | Status |
|----------|------|------------------|-----------|--------|
| OPIM-5771-2025-SP.course_core.md | MD | Course core file example | Grounded Knowledge | **Illustrative** |
| OPIM-5771-2025-SP.student_profile.md | MD | Student profile file example | Grounded Knowledge | **Illustrative** |

---

## System Templates and Profiles

| Filename | Type | Inferred Purpose | Subsystem | Status |
|----------|------|------------------|-----------|--------|
| AI_Course_Assisstant_Instructions_Template.md | MD | Agent instruction template (current version) | Agent Configuration | **Template - Authoritative** |
| Writing_Style_Profile_Josh.md | MD | Student writing style profile and preferences | Student Profile | **Authoritative** |

---

## Current System Reconstruction

### Observed Architecture (from illustrative examples)

**Grounded Knowledge Files Pattern (3-file system)**:
1. `{course_id}.course_core.md` - Contains course policies, grading, structure, instructor information
2. `{course_id}.course_schedule.md` - Contains dates, deadlines, module sequence, assignment calendar
3. `{course_id}.student_profile.md` - Contains student profile, preferences, constraints, progress tracking

**Working Memory Files Pattern**:
- Module folders uploaded as needed (evidenced by tree structure)
- Original PDF syllabi as reference
- Assignment materials, readings, slides within module packages

**Agent Instructions**:
- Template exists at `AI_Course_Assisstant_Instructions_Template.md`
- Intended to be customized per course build
- References NotebookLM as companion tool for longer documents

### How the Current System Works

1. **Setup Phase**:
   - Course core extracted from syllabus (policies, grading, structure)
   - Course schedule extracted from syllabus (dates, deadlines, modules)
   - Student profile compiled from student information and preferences
   - Agent instructions customized with course_id and term_id
   - Files uploaded to custom GPT as Grounded Knowledge

2. **Operational Phase**:
   - Student uploads module content as Working Memory Files
   - Agent references course_core for facts, policies, grading
   - Agent references course_schedule for dates, deadlines, calendar
   - Agent references student_profile for preferences, constraints, progress
   - Agent uses module content for assignment execution support
   - NotebookLM used for deep reading analysis of longer PDFs

3. **Retrieval Behavior**:
   - Agent searches across all uploaded files
   - No explicit indexing system observed
   - No structured citation protocol
   - No validation of retrieved information

### Contradictions and Issues Identified

**1. Inconsistent Date Formatting**:
- MGMT-8001 uses: "Friday, January 26th, 2024"
- IDSC-4444 uses: "Tuesday, August 27, 2024"
- OPIM-5771 uses: "Weds, Jan. 15"
- No standardized display_date/iso_date pair
- No timezone specification

**2. Inconsistent ID Systems**:
- MGMT-8001 uses: `MGMT8001_SP24_MOD01`
- IDSC-4444 uses: `M1`, `M2`, etc. for modules
- OPIM-5771 uses: `Week 1`, `Week 2`
- Assignment IDs often missing entirely
- No deterministic ID generation method

**3. Separation of Concerns**:
- Schedule information now in separate course_schedule file (dates, deadlines)
- Policy information in course_core (grading, rules, structure)
- Student context in student_profile (preferences, progress, constraints)

**4. Ambiguous Authority**:
- No explicit source-of-truth hierarchy
- No conflict resolution rules when course_knowledge and module content disagree
- No protocol for updating information when syllabus changes

**5. Missing Indexing**:
- No INDEX/manifest file
- No section anchors for retrieval
- No way to verify completeness of extracted information
- No referential integrity checks

**6. Personal Information Exposure**:
- MGMT-8001 student_knowledge contains full names of 4 group members
- IDSC-4444 student_knowledge contains full names of 2 group members
- No anonymization or redaction policy

**7. Incomplete Module Integration**:
- Tree structure shows extensive module content for Carlson-School-2025-FA
- No clear protocol for how modules should be uploaded (folder? zip? individual files?)
- No manifest system to track module contents
- No rules for when module content should be cited vs course_core/course_schedule

**8. Assignment Information Gaps**:
- Many assignments lack detailed requirements in course_schedule
- Unclear whether requirements come from syllabus, module files, or both
- No linkage between assignments and module content

**9. Agent Instruction Ambiguities**:
- Template references "course knowledge file(s)" - plural suggests flexibility in count
- No explicit retrieval protocol
- No error handling for missing information
- No guidance on citation formatting

**10. Schema and Validation Absence**:
- No JSON schemas for knowledge files
- No automated validation of file structure
- No checks for required fields
- No date/time format validation

---

## Gaps Requiring Resolution

**Critical Gaps**:
1. No Target Course syllabus or schedule document present for Carlson-School-2025-FA
2. No deterministic assignment ID generation method
3. No INDEX system to optimize retrieval
4. No schema validation system
5. No citation protocol
6. No conflict resolution rules

**Operational Gaps**:
1. No module upload protocol
2. No module manifest system
3. No post-upload verification process
4. No update workflow for course_knowledge when syllabus changes

**Quality Gaps**:
1. No acceptance test suite
2. No retrieval accuracy measurement
3. No validation of extracted information against source
4. No quality checks for completeness

---

## Conventions Requiring Standardization

**Must Standardize**:
- Date/time formats (implement display_date + iso_date + AM/PM times)
- ID generation (course_id, term_id, module_id, assignment_id, etc.)
- File naming patterns
- Section header hierarchy
- Metadata blocks
- Citation format
- Unknown/TBD value representation
- Timezone handling (America/Chicago)

**Must Define**:
- Authority hierarchy
- Update procedures
- Anonymization rules
- Relevance filtering criteria
- Retrieval protocol
- Failure behaviors

---

## Recommended Next Actions

**For Phase 2**:
1. Established 3-file Grounded Knowledge structure: course_core, course_schedule, student_profile
2. Determined module placement (Working Memory Files with manifests)
3. Defined 6-tier source-of-truth hierarchy

**For Phase 3**:
1. Implemented standardized naming and ID system
2. Created INDEX/manifest system (JSON-based)
3. Enforced date/time standards

**For Phase 4-7**:
1. Created templates: 20 (Core), 21 (Schedule), 22 (Profile), 23 (Index), 24 (Module)
2. Built schema validation system (JSON schemas)
3. Developed comprehensive retrieval protocol
4. Revised agent instructions for production use

**Critical Missing Input**:
- Need Carlson-School-2025-FA syllabus and schedule to populate Target Course knowledge files
- Current inventory shows module tree but no authoritative course policy documents