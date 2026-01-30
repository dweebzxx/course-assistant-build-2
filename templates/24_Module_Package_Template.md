# Module Package Template

**Filename Pattern:** `{course_id}.module_{module_id}.module_manifest.md`  
**Regex:** `^[A-Z]{2,10}[0-9]{3,5}\.module_M[0-9]{2}\.module_manifest\.md$`  
**Authority Tier:** 5 (Module content inventory)  
**Example Filename:** `MGMT6022.module_M03.module_manifest.md`

**Purpose:** Inventories all files in a module package and provides module overview information. This is a Working Memory File that supports assignment execution.

---

## Metadata
<!-- anchor: #metadata -->

| Field | Value |
|-------|-------|
| **course_id** | `{COURSE_ID}` |
| **term_id** | `{YYYY}-{TT}` |
| **course_run_id** | `{COURSE_ID}-{YYYY}-{TT}` |
| **module_id** | {MODULE_ID} |
| **module_title** | {Module N: Topic Title} |
| **doc_type** | module_manifest |
| **last_updated** | {YYYY-MM-DD} |

---

## Module Overview
<!-- anchor: #module-overview -->

{Brief 2-3 sentence description of what this module covers and why it matters.}

### Learning Objectives

By the end of this module, you should be able to:

1. {Learning objective 1 - use action verbs: analyze, evaluate, create, apply, etc.}
2. {Learning objective 2}
3. {Learning objective 3}
4. {Learning objective 4 - OPTIONAL}

### Estimated Time

| Activity | Estimated Time |
|----------|----------------|
| Lectures/Videos | {N hours} |
| Readings | {N hours} |
| Assignments | {N hours} |
| **Total** | **{N hours}** |

---

## File Inventory
<!-- anchor: #file-inventory -->

| File Path | Type | Description | Required |
|-----------|------|-------------|----------|
| {module_id}.module_manifest.md | .md | This manifest file | Yes |
| {filename.pdf} | .pdf | {Brief description, e.g., "Lecture notes"} | Yes |
| {filename.md} | .md | {Brief description} | No |
| {filename.txt} | .txt | {Brief description} | No |
| {filename.csv} | .csv | {Brief description} | No |
| {filename.xlsx} | .xlsx | {Brief description} | No |

**Allowed File Types**: `.md`, `.txt`, `.csv`, `.xlsx`, `.pdf` only

**Note:** All files in the module package must be listed in this inventory. Files not in this inventory will not be indexed.

---

## Assignment Links
<!-- anchor: #assignment-links -->

{References to assignments associated with this module. Due dates are authoritative in course_schedule.md.}

| Assignment ID | Title | Type | Due Date Reference |
|---------------|-------|------|-------------------|
| {A##} | {Assignment title} | {individual/quiz/discussion/exam/group/presentation} | course_schedule.md#assignment-calendar |

---

## Notes
<!-- anchor: #notes -->

{Optional: Instructor notes or guidance for this module.}

---

## Index References
<!-- anchor: #index-references -->

This file contains the following sections indexed for retrieval:

| Section Anchor | Section Title |
|----------------|---------------|
| #metadata | Metadata |
| #module-overview | Module Overview |
| #file-inventory | File Inventory |
| #assignment-links | Assignment Links |
| #notes | Notes |
| #index-references | Index References |

---

## Template Validation Checklist

Before finalizing module manifest, verify:

- [ ] course_id matches naming convention (e.g., MGMT6022)
- [ ] term_id follows YYYY-TT format (e.g., 2026-SP)
- [ ] course_run_id follows pattern: {course_id}-{term_id}
- [ ] module_id matches regex: ^M\d{2}$
- [ ] Filename follows pattern: {course_id}.module_{module_id}.module_manifest.md
- [ ] All files in module package are listed in File Inventory
- [ ] All file types are allowed: .md, .txt, .csv, .xlsx, .pdf
- [ ] Assignment IDs match entries in course_schedule.md
- [ ] No dates are listed (dates are in course_schedule.md only)

---

<!--
MODULE PACKAGE TEMPLATE INSTRUCTIONS

FILE NAMING:
- Manifest file: {course_id}.module_{module_id}.module_manifest.md (e.g., MGMT6022.module_M03.module_manifest.md)
- Folder name: {course_id}.module_{module_id}/ (e.g., MGMT6022.module_M03/)
- ZIP name (if zipped): {course_id}.module_{module_id}.zip (e.g., MGMT6022.module_M03.zip)

ALLOWED FILE TYPES:
- .md (Markdown documentation)
- .txt (Plain text)
- .csv (Spreadsheet data)
- .xlsx (Excel spreadsheet)
- .pdf (Documents)

AUTHORITY LEVEL:
- Module manifests are Tier 5 in authority hierarchy
- They do NOT override Grounded Knowledge Files
- Dates in course_schedule.md take precedence

REQUIRED CONTENTS:
- This manifest file ({course_id}.module_{module_id}.module_manifest.md)

AFTER UPLOADING:
1. Prompt agent to scan and verify module contents
2. Update INDEX with new module files
3. Verify all entity IDs are registered in INDEX
-->

---

**END OF TEMPLATE**
