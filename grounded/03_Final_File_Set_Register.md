# Final File Set Register
**Agent Build Scope**: Single course, single term, single student (Josh)  
**Register Date**: 2026-01-25  
**Architecture**: 3-File Grounded Knowledge + INDEX + Working Memory Files  
**Status**: Definitive specification for Phases 3-8

---

## Register Summary

**Total Initial Setup Files**: 4 files  
**Grounded Knowledge Files**: 3 files  
**Required Index/Manifest Files**: 1 file  
**Working Memory File Types**: 2 primary types (modules, ad-hoc)

**Final Grounded Knowledge Files Count (N)**: **3**

1. `{course_id}.course_core.md` - Course policies, grading, structure, instructor
2. `{course_id}.course_schedule.md` - Timeline, due dates, assignments, modules
3. `{course_id}.student_profile.md` - Student context, preferences, group project

---

## GROUNDED KNOWLEDGE FILES

### File Type 1: Course Core

**Purpose**: Authoritative source for course policies, grading system, structure, and instructor information. Rarely updated after term start.

**File Type**: Markdown (.md)

**Naming Rule**:  
Pattern: `{course_id}.course_core.md`  
Regex: `^[A-Z0-9\-]+\.course_core\.md$`  
Example: `CARLSON-SCHOOL-2025-FA.course_core.md`

**Content Outline**:
1. Metadata block (course_id, term_id, doc_type, last_updated, timezone, source_files)
2. Course Identification (title, number, credits, section, term dates)
3. Instructor Information (name, title, contact, office hours)
4. Course Structure (delivery mode, required tools, prerequisites)
5. Grading Policy (components, weights, scale, calculation method)
6. Course Policies (attendance, participation, late work, academic integrity, accommodations)
7. Required Resources (textbooks, software, technology requirements)
8. Learning Objectives (course-level goals)
9. Index References (section linking to INDEX entries)

**Template Filename**: `20_Course_Core_Template.md` (Phase 4 deliverable)

**Schema Filename**: `schema/schema.course_core.json` (Phase 7 deliverable)

**Validation Checks**:
- Required metadata fields present (course_id, term_id, doc_type, last_updated, timezone)
- All section headers match template hierarchy
- All dates use display_date + iso_date pairs
- All times use h:mm AM/PM format
- Grading component weights sum to 100%
- No personal identifying information (except instructor)
- All section anchors are unique and follow pattern: `{#section-name}`

---

### File Type 2: Course Schedule

**Purpose**: Authoritative source for all dates, deadlines, module sequence, and assignment calendar. Single source of truth for temporal information.

**File Type**: Markdown (.md)

**Naming Rule**:  
Pattern: `{course_id}.course_schedule.md`  
Regex: `^[A-Z0-9\-]+\.course_schedule\.md$`  
Example: `CARLSON-SCHOOL-2025-FA.course_schedule.md`

**Content Outline**:
1. Metadata block (course_id, term_id, doc_type, last_updated, timezone, source_files)
2. Term Calendar (start_date, end_date, key deadlines, holidays, exam periods)
3. Module Sequence (module_id, title, topics, start_date, end_date, learning_objectives)
4. Assignment Calendar (assignment_id, title, type, due_date, due_time, points, module_id)
5. Exam Schedule (exam_id, type, date, time, coverage, location)
6. Reading Schedule (reading_id, module_id, source, pages/chapters, due_date)
7. Discussion Schedule (discussion_id, module_id, topic, open_date, close_date)
8. Milestone Timeline (milestone_id, deliverable, due_date, owner)
9. Index References (section linking to INDEX entries)

**Template Filename**: `21_Course_Schedule_Template.md` (Phase 4 deliverable)

**Schema Filename**: `schema/schema.course_schedule.json` (Phase 7 deliverable)

**Validation Checks**:
- Required metadata fields present
- All section headers match template hierarchy
- All dates use display_date + iso_date pairs (BOTH required)
- All times use h:mm AM/PM format with timezone
- All entities have deterministic IDs (module_id, assignment_id, etc.)
- No date conflicts (start_date <= end_date)
- All module_id references are defined in Module Sequence section
- No duplicate IDs within any section
- All section anchors unique

---

### File Type 3: Student Profile

**Purpose**: Authoritative source for student context, preferences, constraints, and group project information. Updated as student discovers preferences.

**File Type**: Markdown (.md)

**Naming Rule**:  
Pattern: `{course_id}.student_profile.md`  
Regex: `^[A-Z0-9\-]+\.student_profile\.md$`  
Example: `CARLSON-SCHOOL-2025-FA.student_profile.md`

**Content Outline**:
1. Metadata block (course_id, term_id, doc_type, last_updated, timezone)
2. Student Core (name: Josh, timezone: America/Chicago)
3. Learning Preferences (communication style, study approach, note-taking, planning)
4. Time Constraints (work schedule, other commitments, availability windows)
5. Technology Profile (access, tools, comfort level)
6. Writing Style Profile (reference to Writing_Style_Profile_Josh.md or inline summary)
7. Course Goals (student-specific objectives)
8. Group Project Context (project_id, role, responsibilities, team structure as Member 01-XX, communication norms, milestone ownership)
9. Known Challenges (subject areas needing support)
10. Progress Tracking (optional: completed modules, current focus)
11. Index References (section linking to INDEX entries)

**Template Filename**: `22_Student_Profile_Template.md` (Phase 4 deliverable)

**Schema Filename**: `schema/schema.student_profile.json` (Phase 7 deliverable)

**Validation Checks**:
- Required metadata fields present
- All section headers match template hierarchy
- Student name is "Josh" only (first name, no last name)
- Timezone is "America/Chicago" or "CT"
- Group project section uses Member 01, Member 02, etc. (no personal names)
- No email addresses, phone numbers, or personal identifiers for group members
- All dates use display_date + iso_date pairs where applicable
- All section anchors unique

---

## REQUIRED INDEX/MANIFEST FILES

### File Type 4: Course Index

**Purpose**: Machine-parseable index enabling section-level retrieval, referential integrity checks, and completeness validation. Links all Grounded Knowledge Files and Working Memory Files.

**File Type**: JSON (.json)

**Naming Rule**:  
Pattern: `{course_id}.index.json`  
Regex: `^[A-Z0-9\-]+\.index\.json$`  
Example: `CARLSON-SCHOOL-2025-FA.index.json`

**Content Outline**:
```json
{
  "index_metadata": {
    "course_id": "string",
    "term_id": "string",
    "index_version": "string (semantic version)",
    "last_updated": "YYYY-MM-DD",
    "timezone": "America/Chicago"
  },
  "grounded_knowledge_files": [
    {
      "filename": "string",
      "doc_type": "course_core | course_schedule | student_profile",
      "last_updated": "YYYY-MM-DD",
      "sections": [
        {
          "section_id": "string (anchor ID)",
          "section_title": "string",
          "section_type": "metadata | policy | schedule | assignment | etc.",
          "entities": [
            {
              "entity_id": "string (module_id, assignment_id, etc.)",
              "entity_type": "module | assignment | exam | reading | discussion | milestone",
              "entity_title": "string",
              "key_fields": {"field_name": "value"}
            }
          ]
        }
      ]
    }
  ],
  "working_memory_files": [
    {
      "module_id": "string",
      "module_title": "string",
      "upload_date": "YYYY-MM-DD",
      "manifest_file": "string (path to module manifest)",
      "files": [
        {
          "filepath": "string (relative path within module package)",
          "filetype": "pdf | pptx | docx | md | etc.",
          "description": "string",
          "indexed": "boolean"
        }
      ]
    }
  ],
  "cross_references": [
    {
      "entity_id": "string",
      "referenced_in": ["filename#section_id", "filename#section_id"]
    }
  ]
}
```

**Template Filename**: `23_Index_Template.json` (Phase 4 deliverable)

**Schema Filename**: `schema/schema.index.json` (Phase 7 deliverable)

**Validation Checks**:
- Valid JSON syntax
- All referenced filenames exist
- All section_id anchors exist in referenced files
- No orphan entity_id (every entity must be defined somewhere)
- No duplicate entity_id within same entity_type
- All cross_references point to valid filename#section_id combinations
- All dates use YYYY-MM-DD format
- Timezone is "America/Chicago"

---

## WORKING MEMORY FILES

### File Type 5: Module Package

**Purpose**: Container for all materials related to a single course module, uploaded as needed during the term. Supports assignment execution and learning.

**File Type**: Folder (directory) or ZIP archive

**Naming Rule**:  
Folder: `{module_id}/`  
ZIP: `{module_id}.zip`  
Regex: `^[A-Z0-9\-]+(/|\.zip)$`  
Example: `CARLSON-FA25-M03/` or `CARLSON-FA25-M03.zip`

**Required Contents**:
- MUST include: `{module_id}.module_manifest.md` (at root of folder/zip)
- MAY include: Any number of PDFs, slides, docs, readings, assignment files, subdirectories

**Content Outline** (for module_manifest.md):
1. Metadata (module_id, module_title, course_id, term_id, last_updated)
2. Module Overview (topics, learning objectives, duration)
3. File Inventory (table listing all files in package with paths, types, descriptions)
4. Assignment Links (references to assignment_id in course_schedule.md)
5. Reading Links (references to reading_id in course_schedule.md)
6. Dependencies (prerequisite modules, required prior knowledge)
7. Notes (instructor notes, known issues, updates)

**Template Filename**: `24_Module_Package_Template.md` (Phase 4 deliverable - for module_manifest.md)

**Schema Filename**: `schema/schema.module_package.json` (Phase 7 deliverable - for module_manifest.md)

**Validation Checks**:
- Module package contains module_manifest.md file
- Manifest module_id matches package name
- All files listed in manifest exist in package
- All files in package are listed in manifest
- All assignment_id references exist in course_schedule.md
- All reading_id references exist in course_schedule.md
- Dates use display_date + iso_date pairs
- No personal identifying information

**Upload Workflow**:
1. Student uploads folder or zip when starting module
2. Student prompts: "Index module {module_id}"
3. Agent locates module_manifest.md, reads file inventory
4. Agent updates INDEX.json with module entries
5. Agent confirms: "Module {module_id} indexed. X files available."

---

### File Type 6: Ad-Hoc Uploaded Files

**Purpose**: Individual files uploaded for specific questions or tasks (example: syllabus PDF, reading article, assignment doc).

**File Type**: Any (PDF, DOCX, PPTX, TXT, MD, etc.)

**Naming Rule**:  
No strict pattern (user-chosen filenames acceptable)  
Recommendation: Use descriptive names, avoid spaces

**Content Outline**: N/A (content is free-form)

**Template Filename**: N/A (not templated)

**Schema Filename**: N/A (not schema-validated)

**Validation Checks**: None (Working Memory Files are not schema-validated)

**Usage**:
- Student uploads file via chat interface
- Student asks question referencing file
- Agent treats as supplementary source (lower authority than Grounded Knowledge Files)
- Agent may cite: "Based on uploaded file [filename]..."
- If contradiction with Grounded Knowledge Files, agent flags conflict

---

## OPTIONAL PROMOTABLE FILE TYPES

### File Type 7: Curated Module Content (Optional)

**Purpose**: If a module proves highly valuable and stable, user may request curation into a structured Grounded Knowledge File.

**File Type**: Markdown (.md)

**Naming Rule**:  
Pattern: `{course_id}.module_{module_id}_curated.md`  
Regex: `^[A-Z0-9\-]+\.module_[A-Z0-9\-]+_curated\.md$`  
Example: `CARLSON-SCHOOL-2025-FA.module_M03_curated.md`

**Promotion Workflow**:
1. Student identifies high-value module content
2. Student requests: "Curate Module {module_id} into Grounded Knowledge"
3. Agent extracts key content following template structure
4. Agent generates curated file
5. User reviews and approves
6. User uploads curated file as Grounded Knowledge
7. Agent updates INDEX, marks curated content as authoritative
8. Original module package remains as Working Memory for completeness

**Template Filename**: `25_Curated_Module_Template.md` (Phase 4 deliverable)

**Schema Filename**: `schema/schema.curated_module.json` (Phase 7 deliverable)

**Validation Checks**: Same as other Grounded Knowledge Files

**Authority**: Once promoted, curated module content has equal authority to other Grounded Knowledge Files and supersedes Working Memory module files for the curated content.

---

## SYSTEM FILES (Not Uploaded to Agent)

### File Type 8: Agent Instructions

**Purpose**: Custom GPT instruction set governing agent behavior, retrieval protocol, and response formatting.

**File Type**: Markdown (.md)

**Naming Rule**: `AI_Course_Assistant_Instructions_{course_id}.md`

**Content Outline**:
1. Agent identity and role
2. Scope constraints (single course, single term, single student)
3. Retrieval protocol (Phase 6 output)
4. Authority hierarchy (from Phase 2 decision memo)
5. Citation requirements
6. Date/time formatting rules
7. Failure behaviors (what to do when information missing)
8. Writing style alignment (reference to Writing_Style_Profile_Josh.md)

**Template Filename**: `AI_Course_Assisstant_Instructions_Template.md` (provided as input, revised in Phase 6)

**Usage**: Paste into Custom GPT instructions field (not uploaded as file)

---

### File Type 9: Writing Style Profile

**Purpose**: Documents Josh's writing preferences, tone, and style for assignment support.

**File Type**: Markdown (.md)

**Naming Rule**: `Writing_Style_Profile_Josh.md`

**Content Outline**: See provided input file

**Usage**: May be uploaded as Grounded Knowledge File OR referenced inline in student_profile.md

---

## FILE SET SUMMARY TABLE

| # | File Type | Purpose | File Format | Authority Tier | Initial Setup | Schema Validated |
|---|-----------|---------|-------------|----------------|---------------|------------------|
| 1 | Course Core | Policies, grading, structure | MD | Tier 2 | Yes | Yes |
| 2 | Course Schedule | Dates, deadlines, timeline | MD | Tier 1 | Yes | Yes |
| 3 | Student Profile | Student context, preferences | MD | Tier 3 | Yes | Yes |
| 4 | Index | Retrieval targeting, integrity | JSON | Tier 4 | Yes (generated) | Yes |
| 5 | Module Package | Module materials container | Folder/ZIP | Tier 6 | No (as needed) | Manifest only |
| 6 | Ad-Hoc Files | Supplementary materials | Any | Tier 6 | No (as needed) | No |
| 7 | Curated Module | Promoted module content | MD | Tier 2 | No (optional) | Yes |
| 8 | Agent Instructions | Agent behavior rules | MD | N/A (system) | Yes (not uploaded) | No |
| 9 | Writing Style | Student writing profile | MD | N/A (reference) | Optional | No |

---

## GROUNDED KNOWLEDGE FILES: FINAL COUNT AND CONTENTS

**Final Grounded Knowledge Files Count (N)**: **3** (initial setup)

**Optional additions**: Curated Module files (0 to N, based on user requests)

### File 1: {course_id}.course_core.md

**Contains**:
- Course identification (title, number, credits, section, term dates)
- Instructor information (name, title, contact, office hours)
- Course structure (delivery mode, tools, prerequisites)
- Grading policy (components, weights, scale, calculation)
- Course policies (attendance, late work, academic integrity, accommodations)
- Required resources (textbooks, software, technology)
- Learning objectives (course-level goals)

**Does NOT contain**:
- Dates and deadlines (→ course_schedule.md)
- Student-specific context (→ student_profile.md)
- Module content (→ Working Memory Files)

---

### File 2: {course_id}.course_schedule.md

**Contains**:
- Term calendar (start, end, key deadlines, holidays)
- Module sequence (IDs, titles, topics, date ranges, objectives)
- Assignment calendar (IDs, titles, types, due dates/times, points, modules)
- Exam schedule (IDs, types, dates/times, coverage, location)
- Reading schedule (IDs, modules, sources, pages, due dates)
- Discussion schedule (IDs, modules, topics, open/close dates)
- Milestone timeline (IDs, deliverables, due dates, owners)

**Does NOT contain**:
- Policies and grading rules (→ course_core.md)
- Assignment detailed requirements (→ Module Working Memory Files or curated assignments)
- Student preferences (→ student_profile.md)

---

### File 3: {course_id}.student_profile.md

**Contains**:
- Student core (name: Josh, timezone)
- Learning preferences (communication, study, note-taking, planning)
- Time constraints (work schedule, commitments, availability)
- Technology profile (access, tools, comfort)
- Writing style profile (inline or reference)
- Course goals (student-specific objectives)
- Group project context (anonymized team structure, roles, norms, milestones)
- Known challenges (subject areas needing support)
- Progress tracking (optional)

**Does NOT contain**:
- Course policies (→ course_core.md)
- Due dates (→ course_schedule.md)
- Personal names of group members (anonymized as Member 01-XX)
- Module content (→ Working Memory Files)

---

## UPDATE TRACKING

**Versioning**: Not required (use last_updated field instead)

**Change Log**: Optional field in each file to document updates

**INDEX Regeneration**: Required after any Grounded Knowledge File update

**Validation**: Run schema validation after every update (Phase 7 validator)

---

## COMPLETION CHECKLIST (For Phase 4-8)

**Phase 4 (Templates)**:
- [ ] 20_Course_Core_Template.md
- [ ] 21_Course_Schedule_Template.md
- [ ] 22_Student_Profile_Template.md
- [ ] 23_Index_Template.json
- [ ] 24_Module_Package_Template.md (module_manifest.md template)
- [ ] 25_Curated_Module_Template.md (optional pathway)

**Phase 5 (Module Protocol)**:
- [ ] Module upload workflow documented
- [ ] Module indexing protocol documented
- [ ] Module manifest requirements documented

**Phase 6 (Retrieval Protocol)**:
- [ ] Section-level retrieval rules
- [ ] Authority hierarchy enforcement
- [ ] Citation format requirements
- [ ] Conflict detection and resolution

**Phase 7 (Schemas)**:
- [ ] schema/schema.course_core.json
- [ ] schema/schema.course_schedule.json
- [ ] schema/schema.student_profile.json
- [ ] schema/schema.index.json
- [ ] schema/schema.module_package.json
- [ ] schema/schema.curated_module.json
- [ ] validate_system.py

**Phase 8 (Setup and Testing)**:
- [ ] Setup prompt sequence
- [ ] Acceptance test suite
- [ ] Validation report

---

## REGISTER APPROVAL

**Status**: Definitive specification  
**Approved by**: Systems Architecture (Phase 2)  
**Date**: 2026-01-25  
**Next Phase**: Phase 3 (Naming and ID Standard)

---

**END OF REGISTER**