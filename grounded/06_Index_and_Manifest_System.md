# Index and Manifest System

**Agent Build Scope:** Single course, single term, single student (Josh)  
**Document Type:** Index and manifest specification  
**Date:** 2026-01-25  
**Phase:** 3  
**Status:** Definitive specification

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
**Pattern:** `{course_id}.index.json`  
**Example:** `MGMT-5001-SEC01-2025-FA.index.json`

### Required Top-Level Fields

```json
{
  "metadata": { ... },
  "files": [ ... ],
  "entities": { ... },
  "sections": [ ... ],
  "cross_references": [ ... ]
}
```

---

## METADATA BLOCK

### Required Fields

```json
"metadata": {
  "course_id": "MGMT-5001-SEC01-2025-FA",
  "term_id": "2025-FA",
  "doc_type": "index",
  "last_updated": "2026-01-25",
  "timezone": "America/Chicago",
  "index_scope": "all_grounded_and_working_files",
  "total_files_indexed": 15,
  "total_sections_indexed": 87,
  "total_entities_indexed": 42
}
```

### Optional Fields

```json
"metadata": {
  "change_log": [
    {
      "date": "2026-01-25",
      "change": "Added Module 5 content",
      "files_affected": ["M05/", "course_schedule.md"]
    },
    {
      "date": "2026-01-20",
      "change": "Updated Assignment A03 due date",
      "files_affected": ["course_schedule.md"]
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
"files": [
  {
    "file_id": "course_core",
    "filename": "MGMT-5001-SEC01-2025-FA.course_core.md",
    "file_type": "grounded_knowledge",
    "doc_type": "course_core",
    "path": "./",
    "last_updated": "2026-01-20",
    "section_count": 12,
    "entity_count": 8,
    "size_bytes": 15420
  },
  {
    "file_id": "course_schedule",
    "filename": "MGMT-5001-SEC01-2025-FA.course_schedule.md",
    "file_type": "grounded_knowledge",
    "doc_type": "course_schedule",
    "path": "./",
    "last_updated": "2026-01-25",
    "section_count": 18,
    "entity_count": 34,
    "size_bytes": 22810
  },
  {
    "file_id": "M03_manifest",
    "filename": "M03.module_manifest.md",
    "file_type": "module_manifest",
    "doc_type": "module_manifest",
    "path": "M03/",
    "module_id": "M03",
    "last_updated": "2026-01-15",
    "section_count": 5,
    "entity_count": 7,
    "size_bytes": 4200
  },
  {
    "file_id": "M03_lecture",
    "filename": "Module_03_Lecture.pptx",
    "file_type": "working_memory",
    "doc_type": "lecture_slides",
    "path": "M03/",
    "module_id": "M03",
    "last_updated": "2026-01-12",
    "section_count": null,
    "entity_count": null,
    "size_bytes": 2048000
  }
]
```

### Required Fields (per file entry)
- `file_id`: Unique identifier for this file (lowercase, underscores allowed)
- `filename`: Exact filename with extension
- `file_type`: One of `grounded_knowledge`, `module_manifest`, `working_memory`
- `doc_type`: Document type (e.g., `course_core`, `assignment_instructions`, `lecture_slides`)
- `path`: Relative path from agent root
- `last_updated`: ISO date (YYYY-MM-DD)

### Optional Fields
- `module_id`: If file belongs to a module
- `section_count`: Number of indexed sections (null if not applicable)
- `entity_count`: Number of indexed entities (null if not applicable)
- `size_bytes`: File size

---

## SECTIONS BLOCK

### Purpose
Index every retrievable section across all files with stable anchor IDs. This is the **primary retrieval mechanism** for the agent.

### Structure

```json
"sections": [
  {
    "section_id": "course_core#metadata",
    "file_id": "course_core",
    "filename": "MGMT-5001-SEC01-2025-FA.course_core.md",
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
    "filename": "MGMT-5001-SEC01-2025-FA.course_core.md",
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
    "filename": "MGMT-5001-SEC01-2025-FA.course_schedule.md",
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
    "filename": "M03.module_manifest.md",
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

## ENTITIES BLOCK

### Purpose
Index every course entity (assignments, modules, exams, readings, discussions, milestones) with its authoritative location and cross-references.

### Structure

```json
"entities": {
  "assignments": [
    {
      "entity_id": "A03",
      "entity_type": "assignment",
      "title": "Marketing Strategy Analysis",
      "authoritative_file": "course_schedule.md",
      "authoritative_section": "course_schedule#assignment-calendar",
      "due_date_display": "Monday, Feb 10, 2026",
      "due_date_iso": "2026-02-10",
      "due_time": "11:59 PM",
      "module_id": "M03",
      "related_sections": [
        "course_schedule#assignment-calendar",
        "M03/Assignment_A03_Instructions.pdf"
      ]
    },
    {
      "entity_id": "EXAM-MIDTERM",
      "entity_type": "exam",
      "title": "Midterm Exam",
      "authoritative_file": "course_schedule.md",
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
  ],
  "readings": [
    {
      "entity_id": "M03-R01",
      "entity_type": "reading",
      "title": "Porter (1980) - Competitive Strategy, Ch. 1",
      "authoritative_file": "course_schedule.md",
      "authoritative_section": "course_schedule#reading-schedule",
      "due_date_display": "Monday, Feb 03, 2026",
      "due_date_iso": "2026-02-03",
      "module_id": "M03",
      "related_sections": [
        "course_schedule#reading-schedule",
        "M03/Reading_Porter_Ch1.pdf"
      ]
    }
  ],
  "discussions": [ ... ],
  "milestones": [
    {
      "entity_id": "PROJ-FINAL-MS01",
      "entity_type": "milestone",
      "title": "Final Project Milestone 1: Team Formation",
      "authoritative_file": "course_schedule.md",
      "authoritative_section": "course_schedule#milestone-timeline",
      "due_date_display": "Friday, Feb 14, 2026",
      "due_date_iso": "2026-02-14",
      "due_time": "5:00 PM",
      "project_id": "PROJ-FINAL",
      "related_sections": [
        "course_schedule#milestone-timeline",
        "student_profile.md#group-project-context"
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

## CROSS_REFERENCES BLOCK

### Purpose
Explicitly map relationships between entities and sections for enhanced retrieval.

### Structure

```json
"cross_references": [
  {
    "from_entity": "A03",
    "to_section": "M03/Assignment_A03_Instructions.pdf",
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
   - Example: `course_schedule.md#assignment-calendar (A03)`

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
  "authoritative_file": "course_schedule.md",
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
  "authoritative_file": "course_schedule.md",
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
  "file_id": "M05_video",
  "filename": "Module_05_Lecture_Video.mp4",
  "file_type": "working_memory",
  "doc_type": "video",
  "path": "M05/",
  "module_id": "M05",
  "last_updated": "2026-02-15",
  "section_count": null,
  "entity_count": null,
  "size_bytes": 104857600
}
```

---

## EXAMPLE: COMPLETE INDEX SNIPPET

```json
{
  "metadata": {
    "course_id": "MGMT-5001-SEC01-2025-FA",
    "term_id": "2025-FA",
    "doc_type": "index",
    "last_updated": "2026-01-25",
    "timezone": "America/Chicago",
    "index_scope": "all_grounded_and_working_files",
    "total_files_indexed": 8,
    "total_sections_indexed": 35,
    "total_entities_indexed": 18
  },
  "files": [
    {
      "file_id": "course_core",
      "filename": "MGMT-5001-SEC01-2025-FA.course_core.md",
      "file_type": "grounded_knowledge",
      "doc_type": "course_core",
      "path": "./",
      "last_updated": "2026-01-20",
      "section_count": 8,
      "entity_count": 0
    },
    {
      "file_id": "course_schedule",
      "filename": "MGMT-5001-SEC01-2025-FA.course_schedule.md",
      "file_type": "grounded_knowledge",
      "doc_type": "course_schedule",
      "path": "./",
      "last_updated": "2026-01-25",
      "section_count": 12,
      "entity_count": 18
    }
  ],
  "sections": [
    {
      "section_id": "course_core#grading-policy",
      "file_id": "course_core",
      "filename": "MGMT-5001-SEC01-2025-FA.course_core.md",
      "anchor": "#grading-policy",
      "section_title": "Grading Policy",
      "section_type": "policy",
      "entity_ids": []
    },
    {
      "section_id": "course_schedule#assignment-calendar",
      "file_id": "course_schedule",
      "filename": "MGMT-5001-SEC01-2025-FA.course_schedule.md",
      "anchor": "#assignment-calendar",
      "section_title": "Assignment Calendar",
      "section_type": "schedule",
      "entity_ids": ["A01", "A02", "A03", "QUIZ-01"]
    }
  ],
  "entities": {
    "assignments": [
      {
        "entity_id": "A03",
        "entity_type": "assignment",
        "title": "Marketing Strategy Analysis",
        "authoritative_file": "course_schedule.md",
        "authoritative_section": "course_schedule#assignment-calendar",
        "due_date_display": "Monday, Feb 10, 2026",
        "due_date_iso": "2026-02-10",
        "due_time": "11:59 PM",
        "module_id": "M03",
        "related_sections": [
          "course_schedule#assignment-calendar",
          "M03/Assignment_A03_Instructions.pdf"
        ]
      }
    ],
    "modules": [
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
        "manifest_file": "M03/M03.module_manifest.md"
      }
    ]
  },
  "cross_references": [
    {
      "from_entity": "A03",
      "to_section": "M03/Assignment_A03_Instructions.pdf",
      "relationship": "detailed_in"
    },
    {
      "from_entity": "M03",
      "to_entity": "A03",
      "relationship": "contains"
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