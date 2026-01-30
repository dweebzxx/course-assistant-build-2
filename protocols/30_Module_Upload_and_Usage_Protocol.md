# Module Upload and Usage Protocol

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Module workflow specification  
**Date:** 2026-01-25  
**Phase:** 5  
**Status:** Definitive specification

---

## PURPOSE

This document defines the mandatory protocol for uploading, organizing, indexing, and utilizing course module content in the Course Assistant AI agent system. Module content constitutes **Working Memory Files** that support assignment execution and provide detailed instructional materials while maintaining clear separation from authoritative course facts stored in Grounded Knowledge Files.

---

## CORE PRINCIPLES

### 1. Module Content = Working Memory Files (Default)

**Default rule:** All module files are Working Memory Files unless explicitly promoted to Grounded Knowledge Files by user instruction.

**Authority tier:** Tier 6 (lowest authority)
- Module content does NOT override Grounded Knowledge Files
- Module content is used for detailed execution support, examples, readings, and instructional materials
- If module content contradicts Grounded Knowledge Files → Grounded Knowledge Files prevail

### 2. One Module Per Package

**Package scope:** Each module is uploaded as a self-contained package (folder or zip) containing all materials for that module.

**No cross-module dependencies in file structure:** Modules reference prerequisites via the module manifest, not via shared folders.

### 3. Module Manifest is Required

**Every module package MUST include a module manifest file** that:
- Inventories all files in the package
- Provides module metadata (title, dates, learning objectives, prerequisites)
- Links to authoritative schedule information in Grounded Knowledge Files

---

## STANDARD MODULE PACKAGE STRUCTURE

### Derived Convention (from Carlson-School-2025-FA.tree.ALL.txt)

Based on analysis of the reference module file tree, the standard module package structure is:

```
{module_id}/
├── {module_id}.module_manifest.md          [REQUIRED]
├── Module_{NN}_Overview.pdf                [OPTIONAL]
├── Module_{NN}_Lecture_Slides.pptx         [OPTIONAL]
├── Module_{NN}_Lecture_Video.mp4           [OPTIONAL]
├── Reading_{Title}.pdf                     [OPTIONAL, multiple allowed]
├── Assignment_{assignment_id}_Instructions.pdf  [OPTIONAL, multiple allowed]
├── Assignment_{assignment_id}_Template.docx     [OPTIONAL]
├── Assignment_{assignment_id}_Rubric.pdf        [OPTIONAL]
├── Discussion_{discussion_id}_Prompt.md         [OPTIONAL]
├── Supplemental_Materials/                      [OPTIONAL subfolder]
│   ├── Example_01.pdf
│   ├── Case_Study.docx
│   └── Data_Files/
└── [Any other instructional files]
```

### Naming Rules

#### Module Folder Name
**Pattern:** `{module_id}/`  
**Examples:**
- `M01/`
- `M03/`
- `M12/`

**Regex:** `^M\d{2}/$`

**Rules:**
- Must match module_id defined in course_schedule.md
- Must be uppercase M followed by 2-digit zero-padded number
- Must end with trailing slash (indicates directory)

#### Module Manifest Filename
**Pattern:** `{module_id}.module_manifest.md`  
**Examples:**
- `M01.module_manifest.md`
- `M03.module_manifest.md`

**Regex:** `^M\d{2}\.module_manifest\.md$`

**Rules:**
- Must exactly match parent module folder name
- Must be placed at root of module folder
- Must be Markdown (.md) format

#### Module Content Files (Recommended Patterns)

**Lecture Slides:**
- Pattern: `Module_{NN}_Lecture_Slides.pptx`
- Example: `Module_03_Lecture_Slides.pptx`

**Lecture Videos:**
- Pattern: `Module_{NN}_Lecture_Video.mp4`
- Example: `Module_03_Lecture_Video.mp4`

**Readings:**
- Pattern: `Reading_{Title}.pdf`
- Example: `Reading_Porter_Ch1.pdf`
- Alternative: `{Author}_{Year}_Ch{N}.pdf`

**Assignment Instructions:**
- Pattern: `Assignment_{assignment_id}_Instructions.pdf`
- Example: `Assignment_A03_Instructions.pdf`

**Assignment Templates:**
- Pattern: `Assignment_{assignment_id}_Template.{ext}`
- Example: `Assignment_A03_Template.docx`

**Assignment Rubrics:**
- Pattern: `Assignment_{assignment_id}_Rubric.pdf`
- Example: `Assignment_A03_Rubric.pdf`

**Discussion Prompts:**
- Pattern: `Discussion_{discussion_id}_Prompt.md`
- Example: `Discussion_D03_Prompt.md`

**Flexibility:** While these patterns are recommended, instructors may use any filenames. The module manifest must accurately inventory all files regardless of naming.

---

## MODULE MANIFEST SPECIFICATION

### Required Location
**Path:** `{module_id}/{module_id}.module_manifest.md`

### Required Sections

Every module manifest must include the following sections with stable anchor IDs:

#### Section 1: Metadata Block
**Anchor:** `#metadata`

**Required fields:**
- `module_id`: Must match folder name exactly
- `module_title`: Human-readable module title
- `course_id`: Reference to course
- `term_id`: Reference to term
- `doc_type`: Must be "module_manifest"
- `last_updated`: ISO date (YYYY-MM-DD)
- `authoritative_schedule_reference`: Section reference to course_schedule.md where this module is defined

**Example:**
```markdown
## Metadata {#metadata}

- **Module ID:** M03
- **Module Title:** Module 3: Competitive Strategy
- **Course ID:** MGMT-5001-SEC01-2025-FA
- **Term ID:** 2025-FA
- **Document Type:** module_manifest
- **Last Updated:** 2026-01-15
- **Authoritative Schedule Reference:** course_schedule.md#module-sequence (M03)
```

#### Section 2: Module Overview
**Anchor:** `#overview`

**Required content:**
- Brief description of module topics
- Learning objectives (3-5 bullet points)
- Estimated time commitment

**Example:**
```markdown
## Module Overview {#overview}

This module explores competitive strategy frameworks including Porter's Five Forces, competitive positioning, and strategic group analysis.

**Learning Objectives:**
- Analyze industry structure using Porter's Five Forces
- Identify sources of competitive advantage
- Evaluate strategic positioning options
- Apply competitive analysis to real-world cases

**Estimated Time:** 8-10 hours
```

#### Section 3: Module Dates
**Anchor:** `#dates`

**Required content:**
- Start date (display_date and iso_date)
- End date (display_date and iso_date)
- Link to authoritative schedule reference

**Example:**
```markdown
## Module Dates {#dates}

- **Start Date (display):** Monday, Feb 03, 2026
- **Start Date (ISO):** 2026-02-03
- **End Date (display):** Sunday, Feb 09, 2026
- **End Date (ISO):** 2026-02-09

**Note:** These dates are for reference only. Authoritative dates are in `course_schedule.md#module-sequence (M03)`.
```

#### Section 4: Prerequisites and Dependencies
**Anchor:** `#prerequisites`

**Required content:**
- List of prerequisite modules (module_id references)
- Required prior knowledge or skills
- "None" if no prerequisites

**Example:**
```markdown
## Prerequisites and Dependencies {#prerequisites}

**Prerequisite Modules:**
- M01 (Introduction to Strategic Management)
- M02 (External Analysis)

**Required Prior Knowledge:**
- Understanding of SWOT analysis
- Familiarity with industry analysis concepts
```

#### Section 5: File Inventory
**Anchor:** `#file-inventory`

**Required content:**
- Complete list of all files in module package
- File description for each file
- File type classification

**Format:**

```markdown
## File Inventory {#file-inventory}

| Filename | Type | Description |
|----------|------|-------------|
| M03.module_manifest.md | manifest | This manifest file |
| Module_03_Lecture_Slides.pptx | lecture_slides | Main lecture presentation (45 slides) |
| Module_03_Lecture_Video.mp4 | lecture_video | Recorded lecture (90 minutes) |
| Reading_Porter_Ch1.pdf | reading | Porter (1980) - Competitive Strategy, Chapter 1 |
| Assignment_A03_Instructions.pdf | assignment_instructions | Detailed instructions for Assignment A03 |
| Assignment_A03_Rubric.pdf | assignment_rubric | Grading rubric for Assignment A03 |
| Discussion_D03_Prompt.md | discussion_prompt | Discussion forum prompt |
| Supplemental_Materials/Case_Study_Tesla.pdf | case_study | Tesla competitive analysis example |
```

**Required table columns:**
1. **Filename:** Exact filename with extension, including subfolder path if applicable
2. **Type:** Classification (lecture_slides, reading, assignment_instructions, etc.)
3. **Description:** Brief human-readable description

**Rules:**
- Every file in the module package must be listed
- Paths must be relative to module root
- Include the manifest itself in the inventory

#### Section 6: Cross-References to Grounded Knowledge Files
**Anchor:** `#cross-references`

**Required content:**
- References to assignment calendar entries for assignments in this module
- References to reading schedule entries
- References to discussion schedule entries
- References to any exam or milestone schedules

**Example:**
```markdown
## Cross-References to Grounded Knowledge Files {#cross-references}

**Assignments:**
- Assignment A03: `course_schedule.md#assignment-calendar (A03)`

**Readings:**
- Reading M03-R01: `course_schedule.md#reading-schedule (M03-R01)`

**Discussions:**
- Discussion D03: `course_schedule.md#discussion-schedule (D03)`

**Related Course Core Sections:**
- Learning objectives alignment: `course_core.md#learning-objectives`
```

### Optional Sections

#### Key Concepts
**Anchor:** `#key-concepts`

List of key terms and concepts introduced in this module.

#### Common Challenges
**Anchor:** `#common-challenges`

Anticipated student difficulties and guidance.

#### Additional Resources
**Anchor:** `#additional-resources`

Optional readings, videos, tools beyond required materials.

---

## MODULE UPLOAD METHODS

### Method 1: Folder Upload (Preferred for Development)

**When to use:**
- Working iteratively with module content
- Frequent updates expected
- Local development and testing

**How to upload:**
1. Create folder with module_id name (e.g., `M03/`)
2. Place all module files in folder
3. Ensure module manifest is present at root
4. Upload entire folder to agent

**Agent file structure after upload:**
```
M03/
├── M03.module_manifest.md
├── Module_03_Lecture_Slides.pptx
├── Reading_Porter_Ch1.pdf
└── Assignment_A03_Instructions.pdf
```

### Method 2: ZIP Upload (Preferred for Distribution)

**When to use:**
- Sharing complete module package
- Archiving modules
- Minimizing upload transactions

**How to upload:**
1. Create folder with module_id name
2. Place all module files in folder
3. Create ZIP archive: `{module_id}.zip`
4. Upload ZIP to agent

**ZIP naming pattern:**
- Pattern: `{module_id}.zip`
- Example: `M03.zip`
- Regex: `^M\d{2}\.zip$`

**Agent behavior after ZIP upload:**
- Extract ZIP to folder matching module_id
- Verify module manifest exists
- Index all files

**ZIP structure (internal):**
```
M03.zip
└── M03/
    ├── M03.module_manifest.md
    ├── Module_03_Lecture_Slides.pptx
    └── [other files]
```

**Important:** ZIP must contain the module folder, not just loose files.

### Method 3: Incremental File Upload (Not Recommended)

**When to use:**
- Only as a last resort if folder/ZIP upload not available

**Process:**
1. Create module folder manually: `M03/`
2. Upload files one at a time into folder
3. Upload manifest last

**Disadvantages:**
- More error-prone
- Requires manual verification
- No atomic package guarantee

---

## POST-UPLOAD WORKFLOW

### Step 1: User Uploads Module Package

User uploads module folder or ZIP using Method 1 or Method 2.

### Step 2: User Runs Module Verification Prompt

**Required prompt (user must run after each module upload):**

```
I have uploaded module package {module_id}. Please verify the module:

1. Confirm that {module_id}.module_manifest.md exists and is readable
2. List all files found in the {module_id}/ folder
3. Compare found files against the File Inventory in the manifest
4. Flag any missing files or extra files not listed in the manifest
5. Verify that cross-references to Grounded Knowledge Files are valid
6. Confirm module_id matches in: folder name, manifest filename, and manifest metadata

Provide a verification report.
```

### Step 3: Agent Provides Verification Report

**Agent must output:**

```
MODULE VERIFICATION REPORT: {module_id}

✅ Manifest found: {module_id}.module_manifest.md
✅ Manifest is readable

Files found in {module_id}/ folder:
1. M03.module_manifest.md
2. Module_03_Lecture_Slides.pptx
3. Reading_Porter_Ch1.pdf
4. Assignment_A03_Instructions.pdf

Inventory check:
✅ All 4 files in manifest are present
✅ No extra files found

Cross-reference validation:
✅ course_schedule.md#assignment-calendar (A03) → Valid
✅ course_schedule.md#reading-schedule (M03-R01) → Valid

Module ID consistency:
✅ Folder name: M03
✅ Manifest filename: M03.module_manifest.md
✅ Manifest metadata module_id: M03

RESULT: Module M03 verification PASSED. Ready for indexing.
```

**If errors found:**

```
MODULE VERIFICATION REPORT: {module_id}

❌ ERRORS DETECTED:

1. Missing file: Assignment_A03_Rubric.pdf (listed in manifest but not found)
2. Extra file found: old_version.pptx (not listed in manifest)
3. Module ID mismatch: Folder name is M03 but manifest metadata says M04

RESULT: Module M03 verification FAILED. Please correct errors and re-upload.
```

### Step 4: User Requests INDEX Update

**Required prompt (user must run after successful verification):**

```
Module {module_id} verification passed. Please update the INDEX:

1. Add {module_id}/ folder entry to the files block
2. Add {module_id}.module_manifest.md entry to the files block
3. Add all sections from the module manifest to the sections block
4. Add {module_id} entry to entities.modules (if not already present)
5. Add cross-references from the manifest to the cross_references block
6. Update metadata: total_files_indexed, total_sections_indexed
7. Set last_updated to today's date

Provide the updated INDEX file.
```

### Step 5: Agent Updates INDEX

**Agent must:**
1. Add new entries to INDEX as specified
2. Validate referential integrity
3. Output complete updated INDEX file: `{course_id}.index.json`

**Example additions to INDEX:**

**files block:**
```json
{
  "file_id": "M03_manifest",
  "filename": "M03.module_manifest.md",
  "file_type": "module_manifest",
  "doc_type": "module_manifest",
  "path": "M03/",
  "module_id": "M03",
  "last_updated": "2026-01-15",
  "section_count": 6,
  "entity_count": 1
}
```

**sections block:**
```json
{
  "section_id": "M03_manifest#file-inventory",
  "file_id": "M03_manifest",
  "filename": "M03.module_manifest.md",
  "anchor": "#file-inventory",
  "section_title": "File Inventory",
  "section_type": "module_file_inventory",
  "parent_section": null,
  "entity_ids": ["M03"]
}
```

**entities.modules:**
```json
{
  "entity_id": "M03",
  "entity_type": "module",
  "title": "Module 3: Competitive Strategy",
  "authoritative_file": "course_schedule.md",
  "authoritative_section": "course_schedule#module-sequence",
  "start_date_display": "Monday, Feb 03, 2026",
  "start_date_iso": "2026-02-03",
  "end_date_display": "Sunday, Feb 09, 2026",
  "end_date_iso": "2026-02-09",
  "module_folder": "M03/",
  "manifest_file": "M03/M03.module_manifest.md",
  "related_sections": [
    "course_schedule#module-sequence",
    "M03/M03.module_manifest.md#overview"
  ]
}
```

### Step 6: User Re-Uploads Updated INDEX

User downloads updated INDEX from agent and re-uploads to agent knowledge files.

---

## MODULE CONTENT USAGE PROTOCOL

### Retrieval Hierarchy for Assignment Questions

When user asks about an assignment (e.g., "What are the requirements for Assignment A03?"):

**Step 1: Consult INDEX**
- Locate assignment entity A03 in `entities.assignments`
- Extract `authoritative_section` (e.g., `course_schedule.md#assignment-calendar`)
- Extract `related_sections` (e.g., `["M03/Assignment_A03_Instructions.pdf"]`)

**Step 2: Consult Grounded Knowledge Files FIRST**
- Retrieve assignment entry from `course_schedule.md#assignment-calendar (A03)`
- Extract: due date, title, module_id, high-level description

**Step 3: Consult Module Files for Detailed Instructions**
- Check `related_sections` for assignment instruction files
- Retrieve detailed requirements from `M03/Assignment_A03_Instructions.pdf`

**Step 4: Synthesize Response**
- State due date and basic info from Grounded Knowledge Files (AUTHORITATIVE)
- Provide detailed requirements from module files (SUPPORTIVE)
- Cite both sources

**Example agent response:**

```
Assignment A03: Marketing Strategy Analysis

**Due Date:** Monday, Feb 10, 2026 at 11:59 PM CT
**Source:** course_schedule.md#assignment-calendar (A03)

**Requirements (from detailed instructions):**
- Length: 5-7 pages, double-spaced
- Format: APA style with title page and references
- Required sections:
  1. Industry analysis using Porter's Five Forces
  2. Competitive positioning analysis
  3. Strategic recommendations (minimum 3)
- Submission: Upload PDF to Canvas

**Rubric:**
- Industry analysis (40 points)
- Competitive positioning (30 points)
- Strategic recommendations (20 points)
- Writing quality and APA formatting (10 points)

**Source:** M03/Assignment_A03_Instructions.pdf (uploaded module content)

Would you like help with any specific section of this assignment?
```

### Handling Contradictions

**Scenario:** Module file states a due date that differs from course_schedule.md.

**Agent behavior:**

```
CONFLICT DETECTED:

course_schedule.md#assignment-calendar (A03) states: Due Monday, Feb 10, 2026 at 11:59 PM
M03/Assignment_A03_Instructions.pdf states: Due February 12, 2026

The Grounded Knowledge File (course_schedule.md) is the authoritative source for dates.

Assignment A03 is due: Monday, Feb 10, 2026 at 11:59 PM CT

Source: course_schedule.md#assignment-calendar (A03) [AUTHORITATIVE]

Note: The module instruction file lists a different date (February 12). If this is a course update, please update course_schedule.md and regenerate the INDEX.
```

**User action required:** User must update course_schedule.md if the date changed, or correct the module file if it contains an error.

---

## MODULE CURATION (OPTIONAL PROMOTION TO GROUNDED KNOWLEDGE FILES)

### When to Curate Module Content

**Scenario 1: Assignment Requirements Change Frequently**

If assignment requirements in module PDFs are updated multiple times per term, consider curating a simplified requirement summary into Grounded Knowledge Files.

**Workflow:**
1. User creates: `{course_id}.module_{module_id}_curated.md`
2. User extracts key assignment requirements from module files
3. User adds to agent as Grounded Knowledge File
4. INDEX is updated to reference curated file as authoritative for requirements

**Example filename:** `MGMT-5001-SEC01-2025-FA.module_M03_curated.md`

**Curated file structure:**
```markdown
## Assignment A03 Requirements {#assignment-a03-requirements}

- **Assignment ID:** A03
- **Module ID:** M03
- **Length:** 5-7 pages
- **Format:** APA, double-spaced
- **Required Sections:**
  1. Industry analysis (Porter's Five Forces)
  2. Competitive positioning
  3. Strategic recommendations (min. 3)
- **Submission Format:** PDF via Canvas
- **Rubric:** See M03/Assignment_A03_Rubric.pdf

**Authoritative Schedule Reference:** course_schedule.md#assignment-calendar (A03)
**Detailed Instructions:** M03/Assignment_A03_Instructions.pdf (supportive)
```

**Important:** Curation is OPTIONAL and ONLY by explicit user instruction. Do not auto-curate.

### When NOT to Curate

**Leave as Working Memory Files (default):**
- Lecture slides (reference material, not authoritative)
- Lecture videos (supplementary)
- Reading PDFs (content, not course facts)
- Case studies and examples
- Supplemental materials
- Templates and tools

---

## AGENT PROMPTS FOR MODULE USAGE

### Prompt 1: What is in Module X?

**User prompt:**
```
What is in Module 3?
```

**Agent response:**

```
Module 3: Competitive Strategy (M03)

**Dates:** Monday, Feb 03, 2026 to Sunday, Feb 09, 2026
Source: course_schedule.md#module-sequence (M03)

**Learning Objectives:**
- Analyze industry structure using Porter's Five Forces
- Identify sources of competitive advantage
- Evaluate strategic positioning options
- Apply competitive analysis to real-world cases

**Module Materials:**
- Lecture slides: Module_03_Lecture_Slides.pptx (45 slides)
- Lecture video: Module_03_Lecture_Video.mp4 (90 minutes)
- Reading: Reading_Porter_Ch1.pdf
- Assignment instructions: Assignment_A03_Instructions.pdf
- Assignment rubric: Assignment_A03_Rubric.pdf
- Discussion prompt: Discussion_D03_Prompt.md
- Case study: Case_Study_Tesla.pdf

**Assignments Due in Module 3:**
- Assignment A03: Due Monday, Feb 10, 2026 at 11:59 PM CT

**Discussions:**
- Discussion D03: Opens Monday, Feb 03, 2026 | Closes Friday, Feb 07, 2026

Source: M03/M03.module_manifest.md#overview, #file-inventory
```

### Prompt 2: Retrieve Specific File from Module

**User prompt:**
```
Show me the discussion prompt for Module 3
```

**Agent response:**

Agent retrieves and displays content from `M03/Discussion_D03_Prompt.md`.

**If file is not text-readable (e.g., PDF, PowerPoint):**

```
The discussion prompt for Module 3 is in:
M03/Discussion_D03_Prompt.md

This file is available in the uploaded module package. I cannot display PDF/PowerPoint content directly, but I can confirm the file exists and you can download it from the module folder.

Would you like me to describe the discussion topic based on the module overview instead?
```

### Prompt 3: Check If All Modules Are Uploaded

**User prompt:**
```
Which modules have been uploaded so far?
```

**Agent response:**

```
Module Upload Status:

Based on INDEX and course_schedule.md, here is the module upload status:

✅ Module 1 (M01): Uploaded (folder: M01/, manifest: M01.module_manifest.md)
✅ Module 2 (M02): Uploaded (folder: M02/, manifest: M02.module_manifest.md)
✅ Module 3 (M03): Uploaded (folder: M03/, manifest: M03.module_manifest.md)
❌ Module 4 (M04): NOT uploaded
❌ Module 5 (M05): NOT uploaded
... (continues for all modules in schedule)

Total modules in course: 12
Uploaded: 3
Remaining: 9

Source: INDEX.json, course_schedule.md#module-sequence
```

---

## EDGE CASES AND MISSING DATA

### Case 1: Module Manifest Missing

**Scenario:** User uploads module folder without a manifest file.

**Agent behavior:**

```
ERROR: Module M05 uploaded without manifest file.

Expected file: M05/M05.module_manifest.md
Status: NOT FOUND

A module manifest is required for every module package. Please create a manifest file using the template and re-upload.

Template: 23_Module_Package_Template.md
```

### Case 2: Manifest Lists Files That Don't Exist

**Scenario:** Manifest file inventory lists 5 files, but only 3 files are present in uploaded folder.

**Agent verification report:**

```
MODULE VERIFICATION REPORT: M06

❌ ERRORS DETECTED:

Missing files (listed in manifest but not found):
1. Assignment_A06_Rubric.pdf
2. Reading_Ch5.pdf

Files found: 3
Files expected (per manifest): 5

RESULT: Module M06 verification FAILED.

Action required: Either upload missing files or update manifest to remove them from inventory.
```

### Case 3: Module Folder Uploaded Without Updating INDEX

**Scenario:** User uploads M07/ folder but does not run INDEX update.

**Agent behavior when user asks about M07:**

```
Module M07 folder appears to be present, but it is not indexed yet.

To use this module, please run the INDEX update workflow:
1. Verify the module using the verification prompt
2. Request INDEX update
3. Re-upload updated INDEX

Until the INDEX is updated, I cannot reliably retrieve or cite content from Module M07.
```

---

## NAMING VALIDATION RULES

### Module Folder Name Validation

**Regex:** `^M\d{2}/$`

**Pass examples:**
- `M01/`
- `M12/`

**Fail examples:**
- `M1/` (not zero-padded)
- `Module_01/` (wrong prefix)
- `m03/` (lowercase)

### Module Manifest Filename Validation

**Regex:** `^M\d{2}\.module_manifest\.md$`

**Pass examples:**
- `M01.module_manifest.md`
- `M10.module_manifest.md`

**Fail examples:**
- `M01_manifest.md` (wrong format)
- `module_manifest.md` (missing module_id)
- `M01.module_manifest.txt` (wrong extension)

### Module ZIP Filename Validation

**Regex:** `^M\d{2}\.zip$`

**Pass examples:**
- `M03.zip`
- `M11.zip`

**Fail examples:**
- `Module_03.zip` (wrong prefix)
- `M3.zip` (not zero-padded)

---

## SUMMARY WORKFLOW DIAGRAM

```
┌─────────────────────────────────────────────────────────────┐
│ USER ACTION: Upload Module Package (Folder or ZIP)         │
│ Example: M03/ or M03.zip                                    │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│ USER PROMPT: Run Module Verification                        │
│ Agent checks: manifest exists, file inventory, IDs match    │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│ AGENT OUTPUT: Verification Report (PASS or FAIL)            │
│ If FAIL: User corrects and re-uploads                       │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼ (If PASS)
┌─────────────────────────────────────────────────────────────┐
│ USER PROMPT: Update INDEX                                   │
│ Agent adds module entries to files, sections, entities      │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│ AGENT OUTPUT: Updated INDEX file                            │
│ User downloads and re-uploads INDEX to agent                │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│ MODULE READY FOR USE                                         │
│ Agent can now retrieve and cite module content               │
└─────────────────────────────────────────────────────────────┘
```

---

## ENFORCEMENT

**Mandatory compliance:**
1. Every module package MUST include a module manifest
2. Module manifest MUST follow the specification above
3. Module folder and manifest filenames MUST match module_id exactly
4. Module verification MUST be run after every upload
5. INDEX MUST be updated after successful verification
6. Agent MUST cite module content using filename and relative path

**No exceptions.**

---

## END OF DOCUMENT