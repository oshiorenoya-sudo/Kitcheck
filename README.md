# KitCheck

My Kitcheck is a Blender tool ( done in Python) that checks game assets before export, starting with naming conventions.

## Status
In progress. The naming check works; a sidebar panel and more checks are planned.

## What works now
- Scans every object in the scene and flags names that don't start with a set prefix
- Returns the list of failing objects

## How to try it
1. Open Blender and go to the Scripting workspace.
2. Open `kitcheck.py` in the Text Editor.
3. In the Python Console, run the script and call `check_names()`.

## Planned
- Sidebar panel with a button
- Scale, material, and poly-count checks
- Batch FBX export

## Built with
Python, Blender Python API (bpy), Git
