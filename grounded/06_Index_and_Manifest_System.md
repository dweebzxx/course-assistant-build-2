# Index and Manifest System

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Index and manifest specification  
**Date:** 2026-01-25  
**Phase:** 3  
**Status:** Partial - Requires revision to align with register specification

**IMPORTANT NOTE:** This document contains outdated structural specifications that predate the definitive File Set Register (03_Final_File_Set_Register.md). The current authoritative specification uses nested sections within `grounded_knowledge_files` rather than separate top-level blocks. This document is being preserved for historical reference but should be updated to match the register specification. **For the current definitive structure, refer to:**
- **03_Final_File_Set_Register.md** (lines 192-246) for the authoritative index structure
- **23_Index_Template.json** for the current template implementation

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
6. **Industry standard:** Widely used for configuration and data interchange (as of January 2026)

**Rejected alternatives:**
- **YAML:** More human-readable but less strict parsing, potential for ambiguity
- **CSV:** Flat structure insufficient for nested entity relationships and cross-references
- **XML:** Verbose, less common in modern agent systems

---

## INDEX FILE SPECIFICATION

### File Naming
**Pattern:** `{course_id}_GK_index.json`  
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
    },
    {
      "date": "2026-01-20",
      "change": "Updated Assignment A03 due date",
      "files_affected": ["MKTG6051_GK_course-schedule.md"]
    }
  ],
  "index_generation_date": "2026-01-25T14:30:00-06:00",
  "index_generator": "manual | script | agent"
}
```

---

## FILES BLOCK

### Purpose
Catalog every file in the agent build (both Grounded Knowledge Files and Working Memory Files) with basic metadata and file location.

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
              "module_id": "M03"
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

**For grounded_knowledge_files:**
- `filename`: Exact filename with extension (must follow `{course_id}_GK_` pattern)
- `doc_type`: One of `course_core`, `course_schedule`, `student_profile`
- `last_updated`: ISO date (YYYY-MM-DD)
- `sections`: Array of section objects with `section_id`, `section_title`, `section_type`, `entities`

**For working_memory_files:**
- `module_id`: Module identifier (e.g., `M01`, `M02`)
- `module_title`: Human-readable module title
- `upload_date`: ISO date (YYYY-MM-DD)
- `manifest_file`: Path to module manifest file
- `files`: Array of file objects with `filepath`, `filetype`, `description`, `indexed`

---

## ⚠️ DEPRECATED: SECTIONS BLOCK

**DEPRECATION NOTICE:** The structure described in this section and all subsequent sections (SECTIONS BLOCK, ENTITIES BLOCK, CROSS_REFERENCES BLOCK) represents an **outdated specification** that has been superseded by the definitive File Set Register.

**Current Specification:** According to 03_Final_File_Set_Register.md (lines 202-246), sections are now nested within the `grounded_knowledge_files` array, not as a separate top-level `sections` block. Entities are also nested within sections with their `key_fields`.

**Action Required:** This section should be completely rewritten to match the register specification. Until then, treat this as **historical documentation only**.

**For current implementation, see:**
- 03_Final_File_Set_Register.md (lines 192-246)
- templates/23_Index_Template.json

---

### [OUTDATED] Purpose
Index every retrievable section across all files with stable anchor IDs. This is the **primary retrieval mechanism** for the agent.

### Structure

```json
"sections": [
  {
    "section_id": "course_core#metadata",
    "file_id": "course_core",
    "filename": "MKTG6051_GK_course-core.md",
    "anchor": "#metadata",
    "section_title": "Metadata",
    "section_type": "metadata_block",
    "parent_section": null,
    "entity_ids": [],
    "char_start": 0,
    "char_end": 420
  },
  {
    "section_id": "course_core#grading-policy",
    "file_id": "course_core",
    "filename": "MKTG6051_GK_course-core.md",
    "anchor": "#grading-policy",
    "section_title": "Grading Policy",
    "section_type": "policy",
    "parent_section": null,
    "entity_ids": [],
    "char_start": 1200,
    "char_end": 3400
  },
  {
    "section_id": "course_schedule#assignment-calendar",
    "file_id": "course_schedule",
    "filename": "MKTG6051_GK_course-schedule.md",
    "anchor": "#assignment-calendar",
    "section_title": "Assignment Calendar",
    "section_type": "schedule",
    "parent_section": null,
    "entity_ids": ["A01", "A02", "A03", "QUIZ-01", "EXAM-MIDTERM"],
    "char_start": 5200,
    "char_end": 12800
  },
  {
    "section_id": "M03_manifest#overview",
    "file_id": "M03_manifest",
    "filename": "MKTG6051_M03.manifest.md",
    "anchor": "#overview",
    "section_title": "Module Overview",
    "section_type": "module_overview",
    "parent_section": null,
    "entity_ids": ["M03"],
    "char_start": 150,
    "char_end": 680
  }
]
```

### Required Fields (per section entry)
- `section_id`: Unique ID in format `{file_id}#{anchor}` (primary key)
- `file_id`: References entry in `files` block
- `filename`: Full filename (for direct citation)
- `anchor`: Section anchor in format `#section-name`
- `section_title`: Human-readable section title
- `section_type`: Classification (e.g., `metadata_block`, `policy`, `schedule`, `assignment_detail`)

### Optional Fields
- `parent_section`: For nested sections (references another `section_id`)
- `entity_ids`: Array of entity IDs defined or referenced in this section
- `char_start`, `char_end`: Character offsets for precise extraction (helpful for chunking)

---

## ⚠️ DEPRECATED: ENTITIES BLOCK

**DEPRECATION NOTICE:** This section describes an outdated structure. Entities are now nested within sections in the `grounded_knowledge_files` array, not as a separate top-level block. See 03_Final_File_Set_Register.md for current specification.

### [OUTDATED] Purpose
Index every course entity (assignments, modules, exams, readings, discussions, milestones) with its authoritative location and cross-references.

### Structure

```json
"entities": {
  "assignments": [
    {
      "entity_id": "A03",
      "entity_type": "assignment",
      "title": "Marketing Strategy Analysis",
      "authoritative_file": "MKTG6051_GK_course-schedule.md",
      "authoritative_section": "course_schedule#assignment-calendar",
      "due_date_display": "Monday, Feb 10, 2026",
      "due_date_iso": "2026-02-10",
      "due_time": "11:59 PM",
      "module_id": "M03",
      "related_sections": [
        "course_schedule#assignment-calendar",
        "MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf"
      ]
    },
    {
      "entity_id": "EXAM-MIDTERM",
      "entity_type": "exam",
      "title": "Midterm Exam",
      "authoritative_file": "MKTG6051_GK_course-schedule.md",
      "authoritative_section": "course_schedule#exam-schedule",
      "due_date_display": "Wednesday, Mar 05, 2026",
      "due_date_iso": "2026-03-05",
      "due_time": "2:00 PM",
      "module_id": null,
      "related_sections": [
        "course_schedule#exam-schedule",
        "course_core#grading-policy"
      ]
    }
  ],
  "modules": [
    {
      "entity_id": "M03",
      "entity_type": "module",
      "title": "Module 3: Competitive Strategy",
      "authoritative_file": "MKTG6051_GK_course-schedule.md",
      "authoritative_section": "course_schedule#module-sequence",
      "start_date_display": "Monday, Feb 03, 2026",
      "start_date_iso": "2026-02-03",
      "end_date_display": "Sunday, Feb 09, 2026",
      "end_date_iso": "2026-02-09",
      "module_folder": "MKTG6051_M03/",
      "manifest_file": "MKTG6051_M03/MKTG6051_M03.manifest.md",
      "related_sections": [
        "course_schedule#module-sequence",
        "MKTG6051_M03/MKTG6051_M03.manifest.md#overview"
      ]
    }
  ],
  "readings": [
    {
      "entity_id": "M03-R01",
      "entity_type": "reading",
      "title": "Porter (1980) - Competitive Strategy, Ch. 1",
      "authoritative_file": "MKTG6051_GK_course-schedule.md",
      "authoritative_section": "course_schedule#reading-schedule",
      "due_date_display": "Monday, Feb 03, 2026",
      "due_date_iso": "2026-02-03",
      "module_id": "M03",
      "related_sections": [
        "course_schedule#reading-schedule",
        "MKTG6051_M03/MKTG6051_M03.R_porter-ch1.pdf"
      ]
    }
  ],
  "discussions": [ ... ],
  "milestones": [
    {
      "entity_id": "PROJ-FINAL-MS01",
      "entity_type": "milestone",
      "title": "Final Project Milestone 1: Team Formation",
      "authoritative_file": "MKTG6051_GK_course-schedule.md",
      "authoritative_section": "course_schedule#milestone-timeline",
      "due_date_display": "Friday, Feb 14, 2026",
      "due_date_iso": "2026-02-14",
      "due_time": "5:00 PM",
      "project_id": "PROJ-FINAL",
      "related_sections": [
        "course_schedule#milestone-timeline",
        "MKTG6051_GK_student-profile.md#group-project-context"
      ]
    }
  ]
}
```

### Required Fields (per entity)
- `entity_id`: Unique entity identifier (as defined in Naming and ID Standard)
- `entity_type`: One of `assignment`, `exam`, `module`, `reading`, `discussion`, `milestone`, `lecture`, `deliverable`
- `title`: Human-readable title
- `authoritative_file`: Filename where this entity is definitively defined
- `authoritative_section`: section_id where this entity is definitively defined

### Conditional Fields
- `due_date_display`, `due_date_iso`, `due_time`: Required for time-bound entities (assignments, exams, discussions, milestones)
- `start_date_display`, `start_date_iso`, `end_date_display`, `end_date_iso`: Required for modules
- `module_id`: Required if entity belongs to a specific module
- `project_id`: Required for milestones

### Optional Fields
- `related_sections`: Array of section_ids or file references where this entity is mentioned or detailed

---

## ⚠️ DEPRECATED: CROSS_REFERENCES BLOCK

**DEPRECATION NOTICE:** This section describes an outdated structure. Cross-references are now handled differently in the current specification. See 03_Final_File_Set_Register.md (lines 240-246) for the current cross_references array format.

### [OUTDATED] Purpose
Explicitly map relationships between entities and sections for enhanced retrieval.

### Structure

```json
"cross_references": [
  {
    "from_entity": "A03",
    "to_section": "MKTG6051_M03/MKTG6051_M03.A_strategy-analysis-instructions.pdf",
    "relationship": "detailed_in"
  },
  {
    "from_entity": "PROJ-FINAL-MS01",
    "to_entity": "PROJ-FINAL",
    "relationship": "milestone_of"
  },
  {
    "from_section": "course_core#grading-policy",
    "to_entity": "EXAM-MIDTERM",
    "relationship": "defines_weight_for"
  },
  {
    "from_entity": "M03",
    "to_entity": "A03",
    "relationship": "contains"
  }
]
```

### Fields
- `from_entity` or `from_section`: Source reference
- `to_entity` or `to_section`: Target reference
- `relationship`: Type of relationship (e.g., `detailed_in`, `milestone_of`, `defines_weight_for`, `contains`, `prerequisite_for`)

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
   - Date/deadline query → Consult `entities.assignments`, `entities.exams`, `entities.milestones`
   - Policy query → Consult `sections` where `section_type = "policy"`
   - Assignment detail query → Consult `entities.assignments` → Follow `related_sections`

2. **Locate entity in INDEX:**
   - Search `entities` block by `entity_id` or `title`
   - Extract `authoritative_section`

3. **Retrieve section content:**
   - Use `sections` block to find `section_id`
   - Extract `filename` and `anchor`
   - Retrieve content from file at specified anchor
   - Optional: Use `char_start` and `char_end` for precise extraction

4. **Cite sources:**
   - Use format: `filename#anchor (entity_id)`
   - Example: `MKTG6051_GK_course-schedule.md#assignment-calendar (A03)`

5. **If content missing or TBD:**
   - State: "Not found in provided materials"
   - Check `related_sections` for supporting content in module files

---

## INDEX VALIDATION REQUIREMENTS

### Automated Validation Checks

**Referential Integrity:**
1. Every `file_id` in `sections` must exist in `files`
2. Every `authoritative_file` in `entities` must exist in `files`
3. Every `authoritative_section` in `entities` must exist in `sections`
4. Every `section_id` in `cross_references` must exist in `sections`
5. Every `entity_id` in `cross_references` must exist in `entities`

**ID Format Compliance:**
1. All `entity_id` values must match regex patterns from Naming and ID Standard
2. All `anchor` values must match `^#[a-z0-9\-]+$`
3. All `section_id` values must match `^[a-z0-9_]+#[a-z0-9\-]+$`

**Date Format Compliance:**
1. All `due_date_iso`, `start_date_iso`, `end_date_iso` must match `YYYY-MM-DD`
2. All `due_date_display` must match `DayOfWeek, Mon DD, YYYY`
3. All `last_updated` must match `YYYY-MM-DD`

**Uniqueness:**
1. All `section_id` values must be unique across entire INDEX
2. All `entity_id` values must be unique within their entity type
3. All `file_id` values must be unique

---

## EDGE CASES AND MISSING DATA POLICY

### When Due Date is TBD

```json
{
  "entity_id": "A07",
  "entity_type": "assignment",
  "title": "Final Reflection Essay",
  "authoritative_file": "MKTG6051_GK_course-schedule.md",
  "authoritative_section": "course_schedule#assignment-calendar",
  "due_date_display": "TBD",
  "due_date_iso": null,
  "due_time": null,
  "module_id": "M12"
}
```

**Agent behavior:** State "Due date: TBD (To Be Determined)" and cite source.

### When Entity Has No Assigned Module

```json
{
  "entity_id": "EXAM-FINAL",
  "entity_type": "exam",
  "title": "Final Exam",
  "authoritative_file": "MKTG6051_GK_course-schedule.md",
  "authoritative_section": "course_schedule#exam-schedule",
  "due_date_display": "Wednesday, May 07, 2026",
  "due_date_iso": "2026-05-07",
  "due_time": "10:00 AM",
  "module_id": null
}
```

**Agent behavior:** Do not force a module association. State "Not associated with a specific module."

### When File is Missing Section Count

For non-text files (PDFs, PowerPoint, images), `section_count` and `entity_count` should be `null`:

```json
{
  "file_id": "M05_lecture",
  "filename": "MKTG6051_M05.L_pricing-strategy.pptx",
  "file_type": "working_memory",
  "doc_type": "lecture_slides",
  "path": "MKTG6051_M05/",
  "module_id": "M05",
  "last_updated": "2026-02-15",
  "section_count": null,
  "entity_count": null,
  "size_bytes": 2048000
}
```

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
                "end_date": "2026-02-09",
                "module_folder": "MKTG6051_M03/",
                "manifest_file": "MKTG6051_M03/MKTG6051_M03.manifest.md"
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
2. What sections exist and how to retrieve them
3. What entities exist and where they are defined
4. How entities and sections relate to each other

**The INDEX is NOT:**
1. A replacement for authoritative content (content lives in Grounded Knowledge Files)
2. A version control system (updates are ad-hoc with `last_updated` tracking)

**Update rule:** Regenerate INDEX after ANY change to Grounded Knowledge Files or module uploads.

---

**END OF DOCUMENT**