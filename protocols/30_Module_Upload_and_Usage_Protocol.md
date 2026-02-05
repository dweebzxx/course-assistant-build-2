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

### Derived Convention

Based on the new file naming standard, the standard module package structure is:

```
{course_id}_M{NN}/
├── {course_id}_M{NN}.manifest.md               [REQUIRED]
├── {course_id}_M{NN}.L_{description}.pptx      [OPTIONAL - Lecture slides]
├── {course_id}_M{NN}.L_{description}.md        [OPTIONAL - Lecture notes]
├── {course_id}_M{NN}.A_{description}.pdf       [OPTIONAL - Assignment instructions]
├── {course_id}_M{NN}.A_{description}.docx      [OPTIONAL - Assignment template]
├── {course_id}_M{NN}.R_{description}.pdf       [OPTIONAL - Resource/reading]
├── {course_id}_M{NN}.B_{description}.pdf       [OPTIONAL - Business case]
└── [Any other instructional files following naming convention]
```

**Example (MKTG6051 Module 03):**
```
MKTG6051_M03/
├── MKTG6051_M03.manifest.md
├── MKTG6051_M03.L_competitive-strategy.pptx
├── MKTG6051_M03.A_strategy-analysis-instructions.pdf
├── MKTG6051_M03.A_strategy-analysis-rubric.pdf
├── MKTG6051_M03.R_porter-five-forces.pdf
├── MKTG6051_M03.R_competitive-positioning.pdf
└── MKTG6051_M03.B_tesla-case-study.docx
```

### Naming Rules

#### Universal File Naming Convention
**Format:** `{CourseID}_M{ModuleNumber}.{TypeCode}_{short-description}.{extension}`

**Type Codes:**
- `.A` = Assignment (instructions, rubric, template, submission)
- `.L` = Lecture (slides, notes, video transcripts)
- `.R` = Resource (article, book, video transcript, etc.)
- `.B` = Business case

**Examples:**
- `MKTG6051_M01.A_chapter-12-questions.md`
- `MKTG6051_M02.L_survey-design.pptx`
- `MKTG6051_M02.R_demand-and-supply.pdf`
- `MKTG6051_M02.B_airbus-v-boeing.docx`

**Regex (module content):** `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.[ALRB]_[a-z0-9\-]+\.[a-z]+$`

#### Course-Level Files (GK)
For course-wide materials (syllabus, schedule), use `GK` instead of module number:
- Pattern: `{CourseID}_GK_{short-description}.{extension}`
- Example: `MKTG6051_GK_syllabus.pdf`

#### Module Folder Name
**Pattern:** `{course_id}_M{NN}/`  
**Examples:**
- `MKTG6051_M01/`
- `MKTG6051_M03/`
- `MGMT6022_M12/`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}/$`

**Rules:**
- Must start with course_id
- Must include module_id (M01, M02, etc.)
- Must end with trailing slash (indicates directory)

#### Module Manifest Filename
**Pattern:** `{course_id}_M{NN}.manifest.md`  
**Examples:**
- `MKTG6051_M01.manifest.md`
- `MKTG6051_M03.manifest.md`
- `MGMT6022_M05.manifest.md`

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.manifest\.md$`

**Rules:**
- Must exactly match parent module folder name
- Must be placed at root of module folder
- Must be Markdown (.md) format

### Allowed File Types

**REQUIRED:** All files in module packages must be one of the following types:

| Extension | Type | Description |
|-----------|------|-------------|
| `.md` | Markdown | Documentation, prompts, notes |
| `.txt` | Plain text | Notes, code snippets, data |
| `.csv` | CSV | Spreadsheet data, tables |
| `.xlsx` | Excel | Spreadsheet data, templates |
| `.pdf` | PDF | Documents, readings, instructions |
| `.pptx` | PowerPoint | Lecture slides |
| `.docx` | Word | Documents, templates |

**Rationale:** Supporting common document formats ensures compatibility with standard course materials while maintaining manageable file processing.

---

## MODULE MANIFEST SPECIFICATION

### Required Location
**Path:** `{course_id}_M{NN}/{course_id}_M{NN}.manifest.md`

**Examples:**
- `MKTG6051_M03/MKTG6051_M03.manifest.md`
- `MGMT6022_M05/MGMT6022_M05.manifest.md`

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
- **Course ID:** MKTG6051
- **Term ID:** 2026-SP
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
- Complete list of all files in module package using new naming convention
- File description for each file
- Type code classification (A, L, R, B)

**Format (using new naming convention):**

```markdown
## File Inventory {#file-inventory}

| Filename | Type Code | Description |
|----------|-----------|-------------|
| MKTG6051_M03.manifest.md | - | This manifest file |
| MKTG6051_M03.L_competitive-strategy.pptx | L | Main lecture presentation (45 slides) |
| MKTG6051_M03.A_strategy-analysis-instructions.pdf | A | Detailed instructions for Assignment A03 |
| MKTG6051_M03.A_strategy-analysis-rubric.pdf | A | Grading rubric for Assignment A03 |
| MKTG6051_M03.R_porter-ch1.pdf | R | Porter (1980) - Competitive Strategy, Chapter 1 |
| MKTG6051_M03.B_tesla-case-study.pdf | B | Tesla competitive analysis example |
```

**Type Codes:**
- `A` = Assignment (instructions, rubric, template)
- `L` = Lecture (slides, notes)
- `R` = Resource (reading, article, reference)
- `B` = Business case

**Required table columns:**
1. **Filename:** Exact filename following pattern: `{CourseID}_M{NN}.{TypeCode}_{description}.{ext}`
2. **Type Code:** Classification code (A, L, R, B, or - for manifest)
3. **Description:** Brief human-readable description

**Rules:**
- Every file in the module package must be listed
- All files must follow the naming convention
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
1. Create folder with course-prefixed module name (e.g., `MKTG6051_M03/`)
2. Place all module files in folder following naming convention
3. Ensure module manifest is present at root
4. Upload entire folder to agent

**Agent file structure after upload:**
```
MKTG6051_M03/
├── MKTG6051_M03.manifest.md
├── MKTG6051_M03.L_competitive-strategy.pptx
├── MKTG6051_M03.R_porter-ch1.pdf
└── MKTG6051_M03.A_strategy-analysis-instructions.pdf
```

### Method 2: ZIP Upload (Preferred for Distribution)

**When to use:**
- Sharing complete module package
- Archiving modules
- Minimizing upload transactions

**How to upload:**
1. Create folder with course-prefixed module name
2. Place all module files in folder following naming convention
3. Create ZIP archive: `{course_id}_M{NN}.zip`
4. Upload ZIP to agent

**ZIP naming pattern:**
- Pattern: `{course_id}_M{NN}.zip`
- Example: `MKTG6051_M03.zip`
- Regex: `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.zip$`

**Agent behavior after ZIP upload:**
- Extract ZIP to folder matching module name
- Verify module manifest exists
- Index all files

**ZIP structure (internal):**
```
MKTG6051_M03.zip
└── MKTG6051_M03/
    ├── MKTG6051_M03.manifest.md
    ├── MKTG6051_M03.L_competitive-strategy.pptx
    └── [other files following naming convention]
```

**Important:** ZIP must contain the module folder, not just loose files.

### Method 3: Incremental File Upload (Not Recommended)

**When to use:**
- Only as a last resort if folder/ZIP upload not available

**Process:**
1. Create module folder manually: `MKTG6051_M03/`
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

1. Confirm that {course_id}_M{NN}.manifest.md exists and is readable
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

✅ Manifest found: {course_id}_M{NN}.manifest.md
✅ Manifest is readable

Files found in {module_id}/ folder:
1. MKTG6051_M03.manifest.md
2. MKTG6051_M03.L_competitive-strategy.pptx
3. Reading_Porter_Ch1.pdf
4. MKTG6051_M03.A_strategy-analysis-instructions.pdf

Inventory check:
✅ All 4 files in manifest are present
✅ No extra files found

Cross-reference validation:
✅ course_schedule.md#assignment-calendar (A03) → Valid
✅ course_schedule.md#reading-schedule (M03-R01) → Valid

Module ID consistency:
✅ Folder name: M03
✅ Manifest filename: MKTG6051_M03.manifest.md
✅ Manifest metadata module_id: M03

RESULT: Module M03 verification PASSED. Ready for indexing.
```

**If errors found:**

```
MODULE VERIFICATION REPORT: {module_id}

❌ ERRORS DETECTED:

1. Missing file: MKTG6051_M03.A_strategy-analysis-rubric.pdf (listed in manifest but not found)
2. Extra file found: old_version.pptx (not listed in manifest)
3. Module ID mismatch: Folder name is M03 but manifest metadata says M04

RESULT: Module M03 verification FAILED. Please correct errors and re-upload.
```

### Step 4: User Requests INDEX Update

**Required prompt (user must run after successful verification):**

```
Module {module_id} verification passed. Please update the INDEX:

1. Add {module_id}/ folder entry to the files block
2. Add {course_id}_M{NN}.manifest.md entry to the files block
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
  "filename": "MKTG6051_M03.manifest.md",
  "file_type": "module_manifest",
  "doc_type": "module_manifest",
  "path": "MKTG6051_M03/",
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
  "filename": "MKTG6051_M03.manifest.md",
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
  "module_folder": "MKTG6051_M03/",
  "manifest_file": "M03/MKTG6051_M03.manifest.md",
  "related_sections": [
    "course_schedule#module-sequence",
    "M03/MKTG6051_M03.manifest.md#overview"
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
- Extract `related_sections` (e.g., `["MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf"]`)

**Step 2: Consult Grounded Knowledge Files FIRST**
- Retrieve assignment entry from `course_schedule.md#assignment-calendar (A03)`
- Extract: due date, title, module_id, high-level description

**Step 3: Consult Module Files for Detailed Instructions**
- Check `related_sections` for assignment instruction files
- Retrieve detailed requirements from `MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf`

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

**Source:** MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf (uploaded module content)

Would you like help with any specific section of this assignment?
```

### Handling Contradictions

**Scenario:** Module file states a due date that differs from course_schedule.md.

**Agent behavior:**

```
CONFLICT DETECTED:

course_schedule.md#assignment-calendar (A03) states: Due Monday, Feb 10, 2026 at 11:59 PM
MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf states: Due February 12, 2026

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
1. User creates: `{course_id}_M{NN}_curated.md`
2. User extracts key assignment requirements from module files
3. User adds to agent as Grounded Knowledge File
4. INDEX is updated to reference curated file as authoritative for requirements

**Example filename:** `MKTG6051-2026-SP_M03_curated.md`

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
- **Rubric:** See MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-rubric.pdf

**Authoritative Schedule Reference:** course_schedule.md#assignment-calendar (A03)
**Detailed Instructions:** MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf (supportive)
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
- Lecture slides: MKTG6051_M03.L_competitive-strategy.pptx (45 slides)
- Lecture video: MKTG6051_M03.L_competitive-strategy-video.mp4 (90 minutes)
- Reading: Reading_Porter_Ch1.pdf
- Assignment instructions: MKTG6051_M03.A_strategy-analysis-instructions.pdf
- Assignment rubric: MKTG6051_M03.A_strategy-analysis-rubric.pdf
- Discussion prompt: Discussion_D03_Prompt.md
- Case study: Case_Study_Tesla.pdf

**Assignments Due in Module 3:**
- Assignment A03: Due Monday, Feb 10, 2026 at 11:59 PM CT

**Discussions:**
- Discussion D03: Opens Monday, Feb 03, 2026 | Closes Friday, Feb 07, 2026

Source: M03/MKTG6051_M03.manifest.md#overview, #file-inventory
```

### Prompt 2: Retrieve Specific File from Module

**User prompt:**
```
Show me the discussion prompt for Module 3
```

**Agent response:**

Agent retrieves and displays content from `MKTG6051_M03/MKTG6051_M03.discussion-prompt.md`.

**If file is not text-readable (e.g., PDF, PowerPoint):**

```
The discussion prompt for Module 3 is in:
MKTG6051_M03/MKTG6051_M03.discussion-prompt.md

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

✅ Module 1 (M01): Uploaded (folder: MKTG6051_M01/, manifest: MKTG6051_M01.manifest.md)
✅ Module 2 (M02): Uploaded (folder: MKTG6051_M02/, manifest: MKTG6051_M02.manifest.md)
✅ Module 3 (M03): Uploaded (folder: M03/, manifest: MKTG6051_M03.manifest.md)
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

Expected file: MKTG6051_M05/MKTG6051_M05.manifest.md
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

**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_M[0-9]{2}\.manifest\.md$`

**Pass examples:**
- `MKTG6051_M01.manifest.md`
- `MKTG6051_M10.manifest.md`

**Fail examples:**
- `M01_manifest.md` (wrong format)
- `module_manifest.md` (missing module_id)
- `MKTG6051_M01.manifest.txt` (wrong extension)

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