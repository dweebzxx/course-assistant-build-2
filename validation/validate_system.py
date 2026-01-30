#!/usr/bin/env python3
"""
Course Assistant System Validator
Validates all generated files against schemas, naming conventions, and referential integrity.
"""

import json
import re
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from datetime import datetime
import jsonschema
from jsonschema import validate, ValidationError, Draft7Validator


class ValidationReport:
    """Stores validation results and generates reports."""
    
    def __init__(self):
        self.errors: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []
        self.successes: List[str] = []
        self.file_count = 0
        self.schema_count = 0
        
    def add_error(self, category: str, file: str, message: str, details: Optional[str] = None):
        self.errors.append({
            'category': category,
            'file': file,
            'message': message,
            'details': details
        })
        
    def add_warning(self, category: str, file: str, message: str):
        self.warnings.append({
            'category': category,
            'file': file,
            'message': message
        })
        
    def add_success(self, message: str):
        self.successes.append(message)
        
    def is_passing(self) -> bool:
        return len(self.errors) == 0
        
    def generate_report(self) -> str:
        """Generate formatted validation report."""
        lines = []
        lines.append("=" * 80)
        lines.append("COURSE ASSISTANT SYSTEM VALIDATION REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Files validated: {self.file_count}")
        lines.append(f"Schemas loaded: {self.schema_count}")
        lines.append("")
        
        # Overall status
        if self.is_passing():
            lines.append("✓ VALIDATION PASSED - No errors found")
        else:
            lines.append(f"✗ VALIDATION FAILED - {len(self.errors)} error(s) found")
        
        lines.append("")
        lines.append(f"Errors: {len(self.errors)}")
        lines.append(f"Warnings: {len(self.warnings)}")
        lines.append(f"Successes: {len(self.successes)}")
        lines.append("")
        
        # Errors section
        if self.errors:
            lines.append("-" * 80)
            lines.append("ERRORS (MUST FIX)")
            lines.append("-" * 80)
            for i, err in enumerate(self.errors, 1):
                lines.append(f"\nError {i}: [{err['category']}]")
                lines.append(f"  File: {err['file']}")
                lines.append(f"  Message: {err['message']}")
                if err['details']:
                    lines.append(f"  Details: {err['details']}")
        
        # Warnings section
        if self.warnings:
            lines.append("")
            lines.append("-" * 80)
            lines.append("WARNINGS (RECOMMENDED FIXES)")
            lines.append("-" * 80)
            for i, warn in enumerate(self.warnings, 1):
                lines.append(f"\nWarning {i}: [{warn['category']}]")
                lines.append(f"  File: {warn['file']}")
                lines.append(f"  Message: {warn['message']}")
        
        # Successes section
        if self.successes:
            lines.append("")
            lines.append("-" * 80)
            lines.append("SUCCESSFUL VALIDATIONS")
            lines.append("-" * 80)
            for success in self.successes:
                lines.append(f"  ✓ {success}")
        
        lines.append("")
        lines.append("=" * 80)
        if self.is_passing():
            lines.append("FINAL RESULT: PASS")
        else:
            lines.append("FINAL RESULT: FAIL")
        lines.append("=" * 80)
        
        return "\n".join(lines)


class SystemValidator:
    """Main validator for Course Assistant system files."""
    
    # Naming convention regex patterns
    NAMING_PATTERNS = {
        'course_id': r'^[A-Z0-9\-]+$',
        'term_id': r'^(20\d{2})-(FA|SP|SU|WI)$',
        'module_id': r'^M\d{2}$',
        'assignment_id': r'^[A-Z]+-?\d{2}(-[A-Z0-9]+)?$',
        'deliverable_id': r'^[A-Z0-9\-]+-DEL\d{2}$',
        'reading_id': r'^(M\d{2}-)?R\d{2}$',
        'milestone_id': r'^([A-Z0-9\-]+-)?MS\d{2}$',
        'project_id': r'^(GP\d{2}|PROJ-[A-Z0-9\-]+)$',
        'member_id': r'^(Member \d{2}|Josh)$',
        'section_id': r'^[a-z0-9_]+#[a-z0-9\-]+$',
        'file_id': r'^[a-z0-9_]+$',
        'anchor': r'^#[a-z0-9\-]+$'
    }
    
    # Date/time patterns
    DATE_PATTERNS = {
        'iso_date': r'^(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$',
        'display_date': r'^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (0[1-9]|[12][0-9]|3[01]), (20\d{2})$',
        'time_12h': r'^(1[0-2]|[1-9]):[0-5][0-9] (AM|PM)$'
    }
    
    # File naming patterns
    FILE_NAMING_PATTERNS = {
        'course_core': r'^[A-Z0-9\-]+_20\d{2}-(FA|SP|SU|WI)_course_core\.md$',
        'student_profile': r'^[A-Z0-9\-]+_20\d{2}-(FA|SP|SU|WI)_student_profile\.md$',
        'index_manifest': r'^[A-Z0-9\-]+_20\d{2}-(FA|SP|SU|WI)_INDEX\.json$',
        'module_manifest': r'^M\d{2}_module_manifest\.md$',
        'assignment_record': r'^[A-Z]+-?\d{2}(-[A-Z0-9]+)?_assignment\.md$',
        'group_project': r'^(GP\d{2}|PROJ-[A-Z0-9\-]+)_project\.md$'
    }
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.schema_path = self.base_path / "schema"
        self.schemas: Dict[str, Dict] = {}
        self.report = ValidationReport()
        
    def load_schemas(self) -> bool:
        """Load all JSON Schema files from schema/ directory."""
        if not self.schema_path.exists():
            self.report.add_error('SCHEMA', 'N/A', f'Schema directory not found: {self.schema_path}')
            return False
            
        schema_files = list(self.schema_path.glob('*.json'))
        
        if not schema_files:
            self.report.add_error('SCHEMA', 'N/A', 'No schema files found in schema/ directory')
            return False
            
        for schema_file in schema_files:
            try:
                with open(schema_file, 'r', encoding='utf-8') as f:
                    schema_data = json.load(f)
                    schema_name = schema_file.stem  # e.g., 'schema.course_knowledge' -> 'schema.course_knowledge'
                    self.schemas[schema_name] = schema_data
                    self.report.schema_count += 1
                    self.report.add_success(f"Loaded schema: {schema_file.name}")
            except json.JSONDecodeError as e:
                self.report.add_error('SCHEMA', schema_file.name, f'Invalid JSON in schema file', str(e))
                return False
            except Exception as e:
                self.report.add_error('SCHEMA', schema_file.name, f'Error loading schema', str(e))
                return False
                
        return True
    
    def validate_against_schema(self, data: Dict, schema_name: str, filename: str) -> bool:
        """Validate data against a specific schema."""
        if schema_name not in self.schemas:
            self.report.add_error('SCHEMA', filename, f'Schema not found: {schema_name}')
            return False
            
        schema = self.schemas[schema_name]
        
        try:
            # Use Draft7Validator for better error messages
            validator = Draft7Validator(schema)
            errors = list(validator.iter_errors(data))
            
            if errors:
                for error in errors:
                    path = " -> ".join(str(p) for p in error.path) if error.path else "root"
                    self.report.add_error(
                        'SCHEMA_VALIDATION',
                        filename,
                        f'Schema validation failed at {path}',
                        error.message
                    )
                return False
            else:
                self.report.add_success(f"Schema validation passed: {filename}")
                return True
                
        except Exception as e:
            self.report.add_error('SCHEMA_VALIDATION', filename, f'Validation error', str(e))
            return False
    
    def validate_naming_convention(self, value: str, pattern_name: str, field_name: str, filename: str) -> bool:
        """Validate a value against a naming convention regex."""
        if pattern_name not in self.NAMING_PATTERNS:
            self.report.add_warning('NAMING', filename, f'Unknown pattern: {pattern_name}')
            return True
            
        pattern = self.NAMING_PATTERNS[pattern_name]
        
        if not re.match(pattern, value):
            self.report.add_error(
                'NAMING_CONVENTION',
                filename,
                f'Invalid {field_name}: "{value}"',
                f'Must match pattern: {pattern}'
            )
            return False
            
        return True
    
    def validate_date_time_fields(self, data: Dict, filename: str, path: str = "") -> bool:
        """Recursively validate date and time fields in data."""
        all_valid = True
        
        if isinstance(data, dict):
            for key, value in data.items():
                current_path = f"{path}.{key}" if path else key
                
                # Check ISO date fields
                if key == 'last_updated' or key.endswith('_date_iso') or key == 'start_date_iso' or key == 'end_date_iso':
                    if value and isinstance(value, str):
                        if not re.match(self.DATE_PATTERNS['iso_date'], value):
                            self.report.add_error(
                                'DATE_FORMAT',
                                filename,
                                f'Invalid ISO date at {current_path}: "{value}"',
                                f'Must match: YYYY-MM-DD'
                            )
                            all_valid = False
                
                # Check display date fields
                elif key.endswith('_date_display') or key == 'start_date_display' or key == 'end_date_display':
                    if value and isinstance(value, str) and value != "TBD":
                        if not re.match(self.DATE_PATTERNS['display_date'], value):
                            self.report.add_error(
                                'DATE_FORMAT',
                                filename,
                                f'Invalid display date at {current_path}: "{value}"',
                                f'Must match: DayOfWeek, Mon DD, YYYY'
                            )
                            all_valid = False
                
                # Check time fields
                elif key.endswith('_time') or key == 'due_time':
                    if value and isinstance(value, str):
                        if not re.match(self.DATE_PATTERNS['time_12h'], value):
                            self.report.add_error(
                                'TIME_FORMAT',
                                filename,
                                f'Invalid time at {current_path}: "{value}"',
                                f'Must match: H:MM AM or H:MM PM'
                            )
                            all_valid = False
                
                # Recurse into nested structures
                elif isinstance(value, (dict, list)):
                    if not self.validate_date_time_fields(value, filename, current_path):
                        all_valid = False
                        
        elif isinstance(data, list):
            for i, item in enumerate(data):
                current_path = f"{path}[{i}]"
                if isinstance(item, (dict, list)):
                    if not self.validate_date_time_fields(item, filename, current_path):
                        all_valid = False
        
        return all_valid
    
    def validate_file_naming(self, filename: str, doc_type: str) -> bool:
        """Validate file naming convention."""
        # Map doc_type to expected pattern
        pattern_map = {
            'course_core': 'course_core',
            'student_profile': 'student_profile',
            'index': 'index_manifest',
            'module_manifest': 'module_manifest',
            'assignment_record': 'assignment_record',
            'group_project': 'group_project'
        }
        
        if doc_type not in pattern_map:
            self.report.add_warning('FILE_NAMING', filename, f'Unknown doc_type: {doc_type}')
            return True
            
        pattern_key = pattern_map[doc_type]
        pattern = self.FILE_NAMING_PATTERNS.get(pattern_key)
        
        if not pattern:
            return True
            
        if not re.match(pattern, filename):
            self.report.add_error(
                'FILE_NAMING',
                filename,
                f'Filename does not match convention',
                f'Expected pattern: {pattern}'
            )
            return False
            
        return True
    
    def validate_referential_integrity(self, index_data: Dict, all_files: Dict[str, Dict]) -> bool:
        """Validate referential integrity between INDEX and referenced files."""
        all_valid = True
        
        # Build lookup maps
        file_lookup = {}
        section_lookup = {}
        entity_lookup = {}
        
        # Index files
        for file_entry in index_data.get('files', []):
            file_id = file_entry.get('file_id')
            filename = file_entry.get('filename')
            if file_id and filename:
                file_lookup[file_id] = filename
        
        # Index sections
        for section in index_data.get('sections', []):
            section_id = section.get('section_id')
            if section_id:
                section_lookup[section_id] = section
        
        # Index entities
        entities = index_data.get('entities', {})
        for entity_type, entity_list in entities.items():
            if isinstance(entity_list, list):
                for entity in entity_list:
                    entity_id = entity.get('entity_id')
                    if entity_id:
                        entity_lookup[entity_id] = entity
        
        # Validate file references
        for file_entry in index_data.get('files', []):
            file_id = file_entry.get('file_id')
            filename = file_entry.get('filename')
            
            # Check if file exists
            if filename and filename not in all_files:
                self.report.add_error(
                    'REFERENTIAL_INTEGRITY',
                    'INDEX.json',
                    f'Referenced file not found: {filename}',
                    f'File ID: {file_id}'
                )
                all_valid = False
        
        # Validate section references
        for section in index_data.get('sections', []):
            section_id = section.get('section_id')
            file_id = section.get('file_id')
            filename = section.get('filename')
            anchor = section.get('anchor')
            
            # Check file_id exists
            if file_id and file_id not in file_lookup:
                self.report.add_error(
                    'REFERENTIAL_INTEGRITY',
                    'INDEX.json',
                    f'Section references unknown file_id: {file_id}',
                    f'Section: {section_id}'
                )
                all_valid = False
            
            # Check filename matches file_id
            if file_id and filename:
                if file_lookup.get(file_id) != filename:
                    self.report.add_error(
                        'REFERENTIAL_INTEGRITY',
                        'INDEX.json',
                        f'Section filename mismatch',
                        f'Section {section_id}: filename={filename}, but file_id {file_id} maps to {file_lookup.get(file_id)}'
                    )
                    all_valid = False
            
            # Validate anchor format
            if anchor and not re.match(self.NAMING_PATTERNS['anchor'], anchor):
                self.report.add_error(
                    'REFERENTIAL_INTEGRITY',
                    'INDEX.json',
                    f'Invalid anchor format: {anchor}',
                    f'Section: {section_id}'
                )
                all_valid = False
        
        # Validate entity references
        for entity_type, entity_list in entities.items():
            if isinstance(entity_list, list):
                for entity in entity_list:
                    entity_id = entity.get('entity_id')
                    auth_file = entity.get('authoritative_file')
                    auth_section = entity.get('authoritative_section')
                    
                    # Check authoritative_file exists
                    if auth_file and auth_file not in [f.get('filename') for f in index_data.get('files', [])]:
                        self.report.add_error(
                            'REFERENTIAL_INTEGRITY',
                            'INDEX.json',
                            f'Entity references unknown file: {auth_file}',
                            f'Entity: {entity_id} ({entity_type})'
                        )
                        all_valid = False
                    
                    # Check authoritative_section exists
                    if auth_section and auth_section not in section_lookup:
                        self.report.add_error(
                            'REFERENTIAL_INTEGRITY',
                            'INDEX.json',
                            f'Entity references unknown section: {auth_section}',
                            f'Entity: {entity_id} ({entity_type})'
                        )
                        all_valid = False
        
        # Validate cross-references
        for xref in index_data.get('cross_references', []):
            from_entity = xref.get('from_entity')
            from_section = xref.get('from_section')
            to_entity = xref.get('to_entity')
            to_section = xref.get('to_section')
            
            if from_entity and from_entity not in entity_lookup:
                self.report.add_error(
                    'REFERENTIAL_INTEGRITY',
                    'INDEX.json',
                    f'Cross-reference from unknown entity: {from_entity}'
                )
                all_valid = False
            
            if from_section and from_section not in section_lookup:
                self.report.add_error(
                    'REFERENTIAL_INTEGRITY',
                    'INDEX.json',
                    f'Cross-reference from unknown section: {from_section}'
                )
                all_valid = False
            
            if to_entity and to_entity not in entity_lookup:
                self.report.add_error(
                    'REFERENTIAL_INTEGRITY',
                    'INDEX.json',
                    f'Cross-reference to unknown entity: {to_entity}'
                )
                all_valid = False
            
            if to_section and to_section not in section_lookup:
                self.report.add_error(
                    'REFERENTIAL_INTEGRITY',
                    'INDEX.json',
                    f'Cross-reference to unknown section: {to_section}'
                )
                all_valid = False
        
        return all_valid
    
    def detect_doc_type(self, data: Dict, filename: str) -> Optional[str]:
        """Detect document type from data."""
        metadata = data.get('metadata', {})
        doc_type = metadata.get('doc_type')
        
        if doc_type:
            return doc_type
        
        # Try to infer from filename
        if 'course_core' in filename:
            return 'course_core'
        elif 'student_profile' in filename:
            return 'student_profile'
        elif 'INDEX' in filename:
            return 'index'
        elif 'module_manifest' in filename:
            return 'module_manifest'
        elif '_assignment' in filename:
            return 'assignment_record'
        elif '_project' in filename:
            return 'group_project'
        
        return None
    
    def validate_file(self, filepath: Path) -> bool:
        """Validate a single file."""
        filename = filepath.name
        self.report.file_count += 1
        
        try:
            # Load file based on extension
            if filepath.suffix == '.json':
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            elif filepath.suffix in ['.md', '.yaml', '.yml']:
                # For now, skip markdown files (would need frontmatter parser)
                # In production, parse YAML frontmatter or structured content
                self.report.add_warning('FILE_TYPE', filename, 'Markdown/YAML validation not yet implemented')
                return True
            else:
                self.report.add_warning('FILE_TYPE', filename, f'Unknown file type: {filepath.suffix}')
                return True
            
            # Detect doc_type
            doc_type = self.detect_doc_type(data, filename)
            
            if not doc_type:
                self.report.add_error('DOC_TYPE', filename, 'Could not detect doc_type')
                return False
            
            # Map doc_type to schema
            schema_map = {
                'course_core': 'schema.course_knowledge',
                'student_profile': 'schema.student_knowledge',
                'index': 'schema.index_manifest',
                'module_manifest': 'schema.module_package',
                'assignment_record': 'schema.assignment_record',
                'group_project': 'schema.group_project'
            }
            
            schema_name = schema_map.get(doc_type)
            
            if not schema_name:
                self.report.add_warning('SCHEMA', filename, f'No schema mapping for doc_type: {doc_type}')
                return True
            
            # Validate against schema
            schema_valid = self.validate_against_schema(data, schema_name, filename)
            
            # Validate file naming
            naming_valid = self.validate_file_naming(filename, doc_type)
            
            # Validate date/time fields
            datetime_valid = self.validate_date_time_fields(data, filename)
            
            return schema_valid and naming_valid and datetime_valid
            
        except json.JSONDecodeError as e:
            self.report.add_error('JSON', filename, 'Invalid JSON', str(e))
            return False
        except Exception as e:
            self.report.add_error('FILE', filename, 'Error reading file', str(e))
            return False
    
    def validate_all(self, target_dir: Optional[str] = None) -> bool:
        """Validate all files in the system."""
        # Load schemas first
        if not self.load_schemas():
            return False
        
        # Determine target directory
        if target_dir:
            search_path = Path(target_dir)
        else:
            search_path = self.base_path
        
        # Find all JSON files (excluding schema directory)
        json_files = []
        for json_file in search_path.rglob('*.json'):
            if 'schema' not in json_file.parts:
                json_files.append(json_file)
        
        # Validate each file
        all_files_data = {}
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    all_files_data[json_file.name] = json.load(f)
            except:
                pass
            
            self.validate_file(json_file)
        
        # Find INDEX file and validate referential integrity
        index_files = [f for f in json_files if 'INDEX' in f.name]
        if index_files:
            for index_file in index_files:
                try:
                    with open(index_file, 'r', encoding='utf-8') as f:
                        index_data = json.load(f)
                    self.validate_referential_integrity(index_data, all_files_data)
                except Exception as e:
                    self.report.add_error('INDEX', index_file.name, 'Error validating referential integrity', str(e))
        
        return self.report.is_passing()


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate Course Assistant system files')
    parser.add_argument('--dir', '-d', default='.', help='Directory to validate (default: current directory)')
    parser.add_argument('--output', '-o', help='Output report to file')
    
    args = parser.parse_args()
    
    validator = SystemValidator(args.dir)
    
    print("Starting Course Assistant System Validation...")
    print(f"Base directory: {validator.base_path.absolute()}")
    print()
    
    is_valid = validator.validate_all()
    
    report = validator.report.generate_report()
    
    print(report)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {args.output}")
    
    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()