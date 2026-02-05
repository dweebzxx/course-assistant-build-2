# Index and Manifest System

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Index and manifest specification  
**Date:** 2026-02-05  
**Phase:** 3  
**Status:** Current - Aligned with File Set Register

---

## PURPOSE

This document defines the mandatory index and manifest system for the Course Assistant AI agent. The INDEX serves as the primary navigation and retrieval mechanism, enabling the agent to locate specific content sections, entities, and references across all Grounded Knowledge Files and Working Memory Files with maximum precision and speed.

---

## INDEX FORMAT DECISION

### Chosen Format: JSON

**Rationale:**
1. **Machine-parseable:** Native support in Python, JavaScript, and all major programming languages
2. **Structured and typed:** Supports nested objects, arrays, and clear data typing
3. **Validation-friendly:** JSON Schema provides robust validation capabilities
4. **Query-capable:** Easy to filter, search, and traverse programmatically
5. **Human-readable:** Readable structure for debugging and manual inspection
6. **Industry standard:** Widely used for configuration and data interchange

**Rejected alternatives:**
- **YAML:** More human-readable but less strict parsing, potential for ambiguity
- **CSV:** Flat structure insufficient for nested entity relationships and cross-references
- **XML:** Verbose, less common in modern agent systems

---

## INDEX FILE SPECIFICATION

### File Naming
**Pattern:** `{course_id}_GK_index.json`  
**Regex:** `^[A-Z]{2,10}[0-9]{3,5}_GK_index\.json$`  
**Example:** `MGMT6022_GK_index.json`

### Required Top-Level Fields

```json
{
  "index_metadata": { ... },
  "grounded_knowledge_files": [ ... ],
  "working_memory_files": [ ... ],
  "cross_references": [ ... ]
}
```

---

## METADATA BLOCK

### Required Fields

```json
"index_metadata": {
  "course_id": "MKTG6051",
  "term_id": "2026-SP",
  "course_run_id": "MKTG6051-2026-SP",
  "index_version": "1.0.0",
  "last_updated": "2026-01-25",
  "timezone": "America/Chicago"
}
```

### Optional Fields

```json
"index_metadata": {
  "change_log": [
    {
      "date": "2026-01-25",
      "change": "Added Module 5 content",
      "files_affected": ["M05/", "MKTG6051_GK_course-schedule.md"]
    }
  ],
  "index_generation_date": "2026-01-25T14:30:00-06:00",
  "index_generator": "manual | script | agent"
}
```

---

## GROUNDED KNOWLEDGE FILES

### Purpose
Catalog all Grounded Knowledge Files with their sections and entities nested within.

### Structure

```json
"grounded_knowledge_files": [
  {
    "filename": "MKTG6051_GK_course-core.md",
    "doc_type": "course_core",
    "last_updated": "2026-01-20",
    "sections": [
      {
        "section_id": "metadata",
        "section_title": "Metadata",
        "section_type": "metadata_block",
        "entities": []
      },
      {
        "section_id": "grading-policy",
        "section_title": "Grading Policy",
        "section_type": "policy",
        "entities": []
      }
    ]
  },
  {
    "filename": "MKTG6051_GK_course-schedule.md",
    "doc_type": "course_schedule",
    "last_updated": "2026-01-25",
    "sections": [
      {
        "section_id": "assignment-calendar",
        "section_title": "Assignment Calendar",
        "section_type": "schedule",
        "entities": [
          {
            "entity_id": "A01",
            "entity_type": "assignment",
            "entity_title": "Marketing Strategy Analysis",
            "key_fields": {
              "due_date": "2026-02-10",
              "due_time": "11:59 PM",
              "module_id": "M03"
            }
          }
        ]
      }
    ]
  }
]
```

### Required Fields

**Per file:**
- `filename`: Exact filename with extension (must follow `{course_id}_GK_` pattern)
- `doc_type`: One of `course_core`, `course_schedule`, `student_profile`
- `last_updated`: ISO date (YYYY-MM-DD)
- `sections`: Array of section objects

**Per section:**
- `section_id`: Unique identifier (anchor without #)
- `section_title`: Human-readable title
- `section_type`: Classification (e.g., `metadata_block`, `policy`, `schedule`)
- `entities`: Array of entity objects (may be empty)

**Per entity:**
- `entity_id`: Unique identifier (e.g., `A01`, `M03`, `EXAM-MIDTERM`)
- `entity_type`: One of `module`, `assignment`, `exam`, `reading`, `discussion`, `milestone`
- `entity_title`: Human-readable title
- `key_fields`: Object containing important fields like dates, times, module_id, etc.

---

## WORKING MEMORY FILES

### Purpose
Catalog module packages and their contents after upload.

### Structure

```json
"working_memory_files": [
  {
    "module_id": "M03",
    "module_title": "Module 3: Competitive Strategy",
    "upload_date": "2026-01-15",
    "manifest_file": "MKTG6051_M03/MKTG6051_M03.manifest.md",
    "files": [
      {
        "filepath": "MKTG6051_M03.A_strategy-analysis-instructions.pdf",
        "filetype": "pdf",
        "description": "Assignment instructions",
        "indexed": true
      },
      {
        "filepath": "MKTG6051_M03.L_competitive-strategy.pptx",
        "filetype": "pptx",
        "description": "Lecture slides",
        "indexed": true
      }
    ]
  }
]
```

### Required Fields

- `module_id`: Module identifier (e.g., `M01`, `M02`)
- `module_title`: Human-readable module title
- `upload_date`: ISO date (YYYY-MM-DD)
- `manifest_file`: Path to module manifest file
- `files`: Array of file objects with `filepath`, `filetype`, `description`, `indexed`

---

## CROSS REFERENCES

### Purpose
Map which files reference specific entities for enhanced retrieval.

### Structure

```json
"cross_references": [
  {
    "entity_id": "A03",
    "referenced_in": [
      "MKTG6051_GK_course-schedule.md#assignment-calendar",
      "MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf"
    ]
  },
  {
    "entity_id": "M03",
    "referenced_in": [
      "MKTG6051_GK_course-schedule.md#module-sequence",
      "MKTG6051_M03/MKTG6051_M03.manifest.md"
    ]
  }
]
```

### Required Fields

- `entity_id`: Entity being referenced
- `referenced_in`: Array of file paths or `filename#section_id` references

---

## INDEX UPDATE WORKFLOW

### When to Regenerate INDEX

**Mandatory regeneration triggers:**
1. Any Grounded Knowledge File is created, updated, or deleted
2. New module package is uploaded
3. New curated module file is created
4. Assignment due date changes
5. New sections or entities are added

**Recommended workflow:**
1. User makes changes to Grounded Knowledge Files or uploads new modules
2. User runs INDEX regeneration script or prompts agent to regenerate
3. Script/agent scans all files, extracts sections and entities, validates IDs
4. New INDEX is generated with updated `last_updated` date
5. Optional: Add entry to `change_log`
6. User uploads new INDEX to agent

### Partial Updates (Advanced)

For efficiency, the system MAY support partial INDEX updates where only changed sections are re-indexed. However, full regeneration is the recommended safe default.

---

## RETRIEVAL PROTOCOL USING INDEX

### Step-by-Step Agent Retrieval Process

1. **Identify query type:**
   - Date/deadline query → Search `grounded_knowledge_files` → `course_schedule` → sections → entities
   - Policy query → Search `grounded_knowledge_files` → `course_core` → sections where `section_type = "policy"`
   - Assignment detail query → Search entities in schedule sections → Use `cross_references` to find related files

2. **Locate entity in INDEX:**
   - Navigate to appropriate grounded knowledge file (course_schedule for assignments/exams/modules)
   - Search through sections to find entity by `entity_id` or `entity_title`
   - Extract entity's `key_fields` for dates, times, etc.

3. **Retrieve section content:**
   - Use the section containing the entity
   - Reference format: `filename#section_id`
   - Extract `filename` and `section_id` to locate content in source file

4. **Find related materials:**
   - Check `cross_references` for the entity_id
   - Follow references to module files and other related content

5. **Cite sources:**
   - Use format: `filename#section_id (entity_id)`
   - Example: `MKTG6051_GK_course-schedule.md#assignment-calendar (A03)`

6. **If content missing or TBD:**
   - State: "Not found in provided materials"
   - Check `cross_references` for supporting content in module files

---

## INDEX VALIDATION REQUIREMENTS

### Automated Validation Checks

**Referential Integrity:**
1. Every `filename` in `grounded_knowledge_files` must exist
2. Every `entity_id` referenced in `cross_references` must exist in grounded_knowledge_files
3. Every file path in `cross_references.referenced_in` should be verifiable
4. Every `manifest_file` in `working_memory_files` should exist

**ID Format Compliance:**
1. All `entity_id` values must match regex patterns from Naming and ID Standard
2. All `section_id` values must be valid anchor identifiers (lowercase, hyphens)
3. All `course_id`, `term_id`, `course_run_id` must match their respective patterns

**Date Format Compliance:**
1. All dates in `key_fields` must use consistent ISO format (YYYY-MM-DD)
2. All `last_updated` fields must match `YYYY-MM-DD`
3. All times should use consistent format (e.g., "11:59 PM")

**Uniqueness:**
1. All `section_id` values must be unique within each file
2. All `entity_id` values must be unique within their entity type
3. All `module_id` values must be unique across working_memory_files

**Completeness:**
1. All required metadata fields must be present
2. All GK files must have at least one section
3. All modules must reference a manifest file

---

## EDGE CASES AND MISSING DATA POLICY

### When Due Date is TBD

```json
{
  "entity_id": "A07",
  "entity_type": "assignment",
  "entity_title": "Final Reflection Essay",
  "key_fields": {
    "due_date": null,
    "due_time": null,
    "module_id": "M12",
    "status": "TBD"
  }
}
```

**Agent behavior:** State "Due date: TBD (To Be Determined)" and cite source section.

### When Entity Has No Assigned Module

```json
{
  "entity_id": "EXAM-FINAL",
  "entity_type": "exam",
  "entity_title": "Final Exam",
  "key_fields": {
    "date": "2026-05-07",
    "time": "10:00 AM",
    "module_id": null
  }
}
```

**Agent behavior:** State "Not associated with a specific module" - do not force a module association.

### When Module Has No Files Yet

```json
{
  "module_id": "M08",
  "module_title": "Module 8: Digital Marketing",
  "upload_date": null,
  "manifest_file": null,
  "files": []
}
```

**Agent behavior:** Acknowledge module exists in schedule but materials not yet uploaded.

---

## EXAMPLE: COMPLETE INDEX SNIPPET

```json
{
  "index_metadata": {
    "course_id": "MKTG6051",
    "term_id": "2026-SP",
    "course_run_id": "MKTG6051-2026-SP",
    "index_version": "1.0.0",
    "last_updated": "2026-01-25",
    "timezone": "America/Chicago"
  },
  "grounded_knowledge_files": [
    {
      "filename": "MKTG6051_GK_course-core.md",
      "doc_type": "course_core",
      "last_updated": "2026-01-20",
      "sections": [
        {
          "section_id": "grading-policy",
          "section_title": "Grading Policy",
          "section_type": "policy",
          "entities": []
        }
      ]
    },
    {
      "filename": "MKTG6051_GK_course-schedule.md",
      "doc_type": "course_schedule",
      "last_updated": "2026-01-25",
      "sections": [
        {
          "section_id": "assignment-calendar",
          "section_title": "Assignment Calendar",
          "section_type": "schedule",
          "entities": [
            {
              "entity_id": "A03",
              "entity_type": "assignment",
              "entity_title": "Marketing Strategy Analysis",
              "key_fields": {
                "due_date": "2026-02-10",
                "due_time": "11:59 PM",
                "module_id": "M03"
              }
            }
          ]
        },
        {
          "section_id": "module-sequence",
          "section_title": "Module Sequence",
          "section_type": "schedule",
          "entities": [
            {
              "entity_id": "M03",
              "entity_type": "module",
              "entity_title": "Module 3: Competitive Strategy",
              "key_fields": {
                "start_date": "2026-02-03",
                "end_date": "2026-02-09"
              }
            }
          ]
        }
      ]
    }
  ],
  "working_memory_files": [
    {
      "module_id": "M03",
      "module_title": "Module 3: Competitive Strategy",
      "upload_date": "2026-01-15",
      "manifest_file": "MKTG6051_M03/MKTG6051_M03.manifest.md",
      "files": [
        {
          "filepath": "MKTG6051_M03.A_strategy-analysis-instructions.pdf",
          "filetype": "pdf",
          "description": "Assignment instructions",
          "indexed": true
        }
      ]
    }
  ],
  "cross_references": [
    {
      "entity_id": "A03",
      "referenced_in": [
        "MKTG6051_GK_course-schedule.md#assignment-calendar",
        "MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf"
      ]
    },
    {
      "entity_id": "M03",
      "referenced_in": [
        "MKTG6051_GK_course-schedule.md#module-sequence",
        "MKTG6051_M03/MKTG6051_M03.manifest.md"
      ]
    }
  ]
}
```

---

## SUMMARY

**The INDEX is the single source of truth for:**
1. What files exist and where they are located
2. What sections exist within each file
3. What entities exist and their key attributes
4. How entities relate to files and modules

**The INDEX is NOT:**
1. A replacement for authoritative content (content lives in Grounded Knowledge Files)
2. A version control system (updates are ad-hoc with `last_updated` tracking)

**Update rule:** Regenerate INDEX after ANY change to Grounded Knowledge Files or module uploads.

**Current specification:** This document aligns with 03_Final_File_Set_Register.md (lines 192-246) and templates/23_Index_Template.json.

---

**END OF DOCUMENT**
