# Final File Set Register - Updated
**Agent Build Scope**: Single course, single term, single student (Josh)  
**Register Date**: 2026-01-25  
**Architecture**: 4-File Grounded Knowledge + INDEX + Working Memory Files  
**Status**: Definitive specification for Phases 3-8

---

## Register Summary

**Total Initial Setup Files**: 5 files  
**Grounded Knowledge Files**: 3 files  
**Required Index/Manifest Files**: 1 file  
**Working Memory File Types**: 1 primary type (module packages)

**Final Grounded Knowledge Files Count (N)**: **3**  
**Index Files Count**: **1**  
**Total Initial Setup Files**: **4**

1. `{course_id}_GK_course-core.md` - Course syllabus, policies, grading, structure, instructor, group project (Tier 1 - highest authority)
2. `{course_id}_GK_course-schedule.md` - Timeline, due dates, assignments, modules (Tier 2 - authoritative for dates)
3. `{course_id}_GK_student-profile.md` - Minimal student context (Tier 3)
4. `{course_id}_GK_index.json` - System index for retrieval (Tier 4)

**Global Naming Rule**: All system-controlled files MUST start with `{course_id}_GK_` for Grounded Knowledge files.

---

## REQUIRED IDENTIFIERS (MUST MATCH NAMING STANDARD)

### course_id
- **Definition**: Course code only (no term, no year, no institution/school names)
- **Example**: `MGMT6022`
- **Regex**: `^[A-Z]{2,10}[0-9]{3,5}$`
- **Explicit non-example**: `CARLSON-SCHOOL` is NOT a course_id

### term_id
- **Definition**: Academic term identifier
- **Example**: `2026-SP`
- **Regex**: `^(20[0-9]{2})-(FA|SP|SU|WI)$`

### course_run_id
- **Definition**: Course instance for a specific term (used in metadata only, not in filenames)
- **Format**: `{course_id}-{term_id}`
- **Example**: `MGMT6022-2026-SP`
- **Regex**: `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA|SP|SU|WI)$`
- **Usage**: Appears in document metadata fields, not in filenames

---

## GROUNDED KNOWLEDGE FILES

### File Type 1: Course Core

**Purpose**: Authoritative source for course syllabus, policies, grading system, structure, instructor information, and group project definition. Tier 1 authority - highest priority for all course requirements.

**File Type**: Markdown (.md)

**Naming Rule**:  
Pattern: `{course_id}_GK_course-core.md`  
Regex: `^[A-Z]{2,10}[0-9]{3,5}_GK_course-core\.md$`  
Example: `MGMT6022_GK_course-core.md`

**Content Outline**:
1. Metadata block (course_id, term_id, course_run_id, doc_type, last_updated, timezone, source_files)
2. Course Identification (title, number, credits, section label if present, term dates)
3. Instructor Information (name, title, contact, office hours)
4. Course Syllabus (complete syllabus content)
5. Course Structure (delivery mode, required tools, prerequisites)
6. Grading Policy (components, weights, scale, calculation method)
7. Course Policies (attendance, participation, late work, academic integrity, accommodations)
8. Required Resources (textbooks, software, technology requirements)
9. Learning Objectives (course-level goals)
10. Group Project Context (yes/no, team name, project ID if applicable)
11. Index References (section linking to INDEX entries)

**Template Filename**: `20_Course_Core_Template.md` (Phase 4 deliverable)

**Schema Filename**: `schema/schema.course_core.json` (Phase 7 deliverable)

**Validation Checks**:
- Required metadata fields present (course_id, term_id, course_run_id, doc_type, last_updated, timezone)
- All section headers match template hierarchy
- Grading component weights sum to 100%
- No personal identifying information (except instructor)
- All section anchors are unique and follow pattern: `{#section-name}`
- Group project context is defined (yes/no selection)

**Does NOT contain**:
- Specific dates and deadlines (→ course-schedule.md is Tier 2 for all temporal information)
- Student-specific context (→ student-profile.md)
- Module content (→ Working Memory Files)

---

### File Type 2: Course Schedule

**Purpose**: Authoritative source for all dates, deadlines, module sequence, and assignment calendar. Tier 2 authority - single source of truth for temporal information.

**File Type**: Markdown (.md)

**Naming Rule**:  
Pattern: `{course_id}_GK_course-schedule.md`  
Regex: `^[A-Z]{2,10}[0-9]{3,5}_GK_course-schedule\.md$`  
Example: `MGMT6022_GK_course-schedule.md`

**Content Outline**:
1. Metadata block (course_id, term_id, course_run_id, doc_type, last_updated, timezone, source_files)
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

**Purpose**: Minimal authoritative source for student context. Portable across courses with minimal editing. Contains only: student identification and comprehensive writing style profile.

**File Type**: Markdown (.md)

**Naming Rule**:  
Pattern: `{course_id}_GK_student-profile.md`  
Regex: `^[A-Z]{2,10}[0-9]{3,5}_GK_student-profile\.md$`  
Example: `MGMT6022_GK_student-profile.md`

**Content Outline**:
1. Metadata block (course_id, term_id, course_run_id, doc_type, last_updated, timezone, student_name)
2. Student Identification (name: Josh, preferred name, program, year label if desired, timezone)
3. Writing Style Profile (comprehensive profile including: Quick Reference Card, Voice & Personality, Sentence Structure Rules, Punctuation Rules, Vocabulary & Word Choice, Tone & Confidence, Opening & Closing Patterns, Transitions & Flow, Formatting Preferences, Context-Based Register Variations, Writing Samples, Common Mistakes to Avoid, Implementation Checklist)
4. Index References (section linking to INDEX entries)

**Template Filename**: `22_Student_Profile_Template.md` (Phase 4 deliverable)

**Schema Filename**: `schema/schema.student_profile.json` (Phase 7 deliverable)

**Validation Checks**:
- Required metadata fields present (course_id, term_id, course_run_id, doc_type, last_updated, timezone, student_name)
- All section headers match template hierarchy
- Student name is "Josh" only (first name, no last name)
- Timezone is "America/Chicago" or "CT"
- All section anchors unique

**Removed Sections** (moved or deprecated):
- Course Goals (deprecated - too course-specific)
- Learning Preferences (deprecated - too variable)
- Schedule and Constraints (deprecated - too variable)
- Technology Profile (deprecated - too variable)
- Progress Tracking (deprecated - too maintenance-heavy)
- Agent Interaction History (deprecated - not needed)
- Communication Preferences (deprecated - use writing style instead)
- Group Project Assignment (moved to course_core.md)
- Team Structure (removed - simplified group project model)
- Milestone Ownership (removed - simplified group project model)
- Known Challenges (removed - not needed)

---

## REQUIRED INDEX/MANIFEST FILES

### File Type 4: Course Index

**Purpose**: Machine-parseable index enabling section-level retrieval, referential integrity checks, and completeness validation. Links all Grounded Knowledge Files and Working Memory Files.

**File Type**: JSON (.json)

**Naming Rule**:  
Pattern: `{course_id}_GK_index.json`  
Regex: `^[A-Z]{2,10}[0-9]{3,5}_GK_index\.json$`  
Example: `MGMT6022_GK_index.json`

**Content Outline**:
```json
{
  "index_metadata": {
    "course_id": "string",
    "term_id": "string",
    "course_run_id": "string",
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
````

**Template Filename**: `23_Index_Template.json` (Phase 4 deliverable)

**Schema Filename**: `schema/schema.index.json` (Phase 7 deliverable)

**Validation Checks**:

* Valid JSON syntax
* All referenced filenames exist
* All section_id anchors exist in referenced files
* No orphan entity_id (every entity must be defined somewhere)
* No duplicate entity_id within same entity_type
* All cross_references point to valid filename#section_id combinations
* All dates use YYYY-MM-DD format
* Timezone is "America/Chicago"

---

## WORKING MEMORY FILES

### File Type 5: Module Package

**Purpose**: Container for all materials related to a single course module, uploaded as needed during the term. Supports assignment execution and learning.

**File Type**: Folder (directory) or ZIP archive

**Naming Rule (MUST start with course_id)**:
Folder: `{course_id}_M{NN}/`
ZIP: `{course_id}_M{NN}.zip`
Regex: `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}(/|\.zip)$`
Examples: `MKTG6051_M03/` or `MKTG6051_M03.zip`

**Required Contents**:

* MUST include: `{course_id}_M{NN}.manifest.md` (at root of folder/zip)
* MAY include: Any number of PDFs, slides, docs, readings, assignment files, subdirectories

**Content Outline** (for module_manifest.md):

1. Metadata (module_id, module_title, course_id, term_id, course_run_id, last_updated)
2. Module Overview (topics, learning objectives, duration)
3. File Inventory (table listing all files in package with paths, types, descriptions)
4. Assignment Links (references to assignment_id in course_schedule.md)
5. Reading Links (references to reading_id in course_schedule.md)
6. Dependencies (prerequisite modules, required prior knowledge)
7. Notes (instructor notes, known issues, updates)

**Module Manifest Naming Rule**:
Pattern: `{course_id}_M{NN}.manifest.md`
Regex: `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.manifest\.md$`
Example: `MKTG6051_M03.manifest.md`

**Template Filename**: `24_Module_Package_Template.md` (Phase 4 deliverable - for module_manifest.md)

**Schema Filename**: `schema/schema.module_package.json` (Phase 7 deliverable - for module_manifest.md)

**Validation Checks**:

* Module package contains module_manifest.md file
* Manifest module_id matches module_id in package name
* All files listed in manifest exist in package
* All files in package are listed in manifest
* All assignment_id references exist in course_schedule.md
* All reading_id references exist in course_schedule.md
* Dates use display_date + iso_date pairs
* No personal identifying information

**Upload Workflow**:

1. Student uploads folder or zip when starting module
2. Student prompts: "Index module {module_id}"
3. Agent locates module_manifest.md, reads file inventory
4. Agent updates `{course_run_id}.index.json` with module entries
5. Agent confirms: "Module {module_id} indexed. X files available."

---

### File Type 6: Ad-Hoc Uploaded Files

**Purpose**: Individual files uploaded for specific questions or tasks (example: syllabus PDF, reading article, assignment doc).

**File Type**: Any (PDF, DOCX, PPTX, TXT, MD, etc.)

**Naming Rule**:
No strict pattern (user-chosen filenames acceptable)
Recommendation: Use descriptive names, avoid spaces

**Validation Checks**: None (ad-hoc uploads are not schema-validated)

**Usage**:

* Student uploads file via chat interface
* Student asks question referencing file
* Agent treats as supplementary source (lower authority than Grounded Knowledge Files)
* If contradiction with Grounded Knowledge Files, agent flags conflict

---

## OPTIONAL PROMOTABLE FILE TYPES

### File Type 7: Curated Module Content (Optional)

**Purpose**: If a module proves highly valuable and stable, user may request curation into a structured Grounded Knowledge File.

**File Type**: Markdown (.md)

**Naming Rule**:
Pattern: `{course_run_id}_M{NN}_curated.md`
Regex: `^[A-Z]{2,10}[0-9]{3,5}-20[0-9]{2}-(FA|SP|SU|WI)_M[0-9]{2}_curated\.md$`
Example: `MKTG6051_M03_curated.md`

**Authority**: Once promoted, curated module content has equal authority to other Grounded Knowledge Files and supersedes Working Memory module files for the curated content.

---

## SYSTEM FILES (Not Uploaded to Agent)

### File Type 8: Agent Instructions

**File Type**: Markdown (.md)

**Naming Rule**: `AI_Course_Assistant_Instructions_{course_run_id}.md`

**Example**: `AI_Course_Assistant_Instructions_MGMT6022.md`

**Usage**: Paste into Custom GPT instructions field (not uploaded as file)

---

### File Type 9: Writing Style Profile

**File Type**: Markdown (.md)

**Naming Rule (optional alignment)**:

* Preferred: `{course_run_id}.writing_style_profile_josh.md`
* Example: `MGMT6022_writing_style_profile_josh.md`

**Note**: This may be embedded into student_profile.md instead of existing as a separate file.

---

## FILE SET SUMMARY TABLE

| # | File Type       | Purpose                                                  | File Format | Authority Tier | Initial Setup   | Schema Validated |
| - | --------------- | -------------------------------------------------------- | ----------- | -------------- | --------------- | ---------------- |
| 1 | Course Core     | Syllabus, policies, grading, structure, group project (highest authority) | MD          | Tier 1         | Yes             | Yes              |
| 2 | Course Schedule | Dates, deadlines, timeline (authoritative for temporal info) | MD          | Tier 2         | Yes             | Yes              |
| 3 | Student Profile | Student identification and comprehensive writing style profile | MD          | Tier 3         | Yes             | Yes              |
| 4 | Index           | Retrieval targeting, integrity                           | JSON        | Tier 4         | Yes (generated) | Yes              |
| 5 | Module Package  | Module materials container                               | Folder/ZIP  | Tier 5         | No (as needed)  | Manifest only    |

**Note**: Assignment details live in course-schedule.md Assignment Calendar. Group project definition and student-specific assignment are both in course-core.md Group Project Context section.

---

## REGISTER APPROVAL

**Status**: Definitive specification
**Approved by**: Systems Architecture (Phase 2)
**Date**: 2026-01-25
**Updated**: 2026-01-30 (Architecture updates: naming standard alignment, writing profile integration, group project consolidation)
**Next Phase**: Phase 3 (Naming and ID Standard)

---

**END OF REGISTER**
