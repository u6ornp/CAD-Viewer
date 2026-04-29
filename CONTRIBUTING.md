# Contributing to CAD Viewer

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful and constructive in all interactions. This project welcomes contributions from everyone.

## Ways to Contribute

### 1. Report Bugs
Found a bug? Help us fix it!

- **Before reporting:** Check existing issues to avoid duplicates
- **Include:**
  - Clear description of the bug
  - Steps to reproduce
  - Expected vs. actual behavior
  - Your system info (OS, Python version, browser)
  - Error messages or screenshots

### 2. Suggest Features
Have an idea for an improvement?

- **Describe:** What feature and why it would be useful
- **Use cases:** When and how users would use it
- **Related features:** Any similar features in other projects

### 3. Improve Documentation
Documentation improvements are always welcome!

- Fix typos or unclear explanations
- Add examples or tutorials
- Clarify installation steps

### 4. Submit Code

## Getting Started

### 1. Fork the Repository
```bash
# Click "Fork" on GitHub
git clone https://github.com/yourusername/CAD-Viewer.git
cd CAD-Viewer
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or for bugs:
git checkout -b fix/bug-description
```

### 3. Make Your Changes
- Keep changes focused and atomic
- Write clean, readable code
- Follow existing code style
- Add comments for complex logic

### 4. Test Your Changes
```bash
python server.py
# Open http://localhost:8080 and test thoroughly
```

### 5. Commit with Clear Messages
```bash
git add .
git commit -m "Brief description of change

- More detailed explanation
- List key changes
- Reference issue #123 if applicable"
```

### 6. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

Then create a PR on GitHub with:
- Descriptive title
- Explanation of changes
- Screenshots if UI changes
- Reference related issues

## Development Setup

```bash
# Python 3.9+ recommended
python --version

# Install optional dependencies for IGES support
pip install pythonocc-core

# Or use FreeCAD as fallback
```

## Code Style

### Python
- Follow PEP 8
- Use 4 spaces for indentation
- Name variables clearly

### JavaScript
- Use 2 spaces for indentation
- Use const/let (not var)
- Follow existing patterns

### Comments
- Keep them brief and meaningful
- Explain WHY, not WHAT
- Update when code changes

## File Structure

```
CAD-Viewer/
├── cad_viewer.html         # Main application (all-in-one)
├── server.py               # Python web server
├── iges_reader/            # Optional IGES support
└── docs/                   # Documentation
```

## Adding Features

### New File Format Support
1. Create new module in appropriate folder
2. Extend `loadFile()` function to detect format
3. Add parser for the format
4. Update documentation
5. Test with sample files

### New UI Controls
1. Add button/control to HTML
2. Implement event handler
3. Add to tooltip/help text
4. Update `HOW_TO_USE.txt`

### New Selection Modes
1. Add mode name to `selectionMode` options
2. Implement logic in viewport click handler
3. Add button in toolbar
4. Update `SELECTION_MODES.md`

## Testing

### Manual Testing Checklist
- [ ] Feature works as intended
- [ ] No errors in browser console
- [ ] Works with different file sizes
- [ ] Works in multiple browsers
- [ ] UI is responsive
- [ ] Edge cases handled

### Test Files
- Use `test-cube.stl` for basic testing
- Test with your own CAD files
- Test with large files (>50MB) if claiming performance improvements

## Performance

When adding features:
- Avoid blocking operations
- Use efficient algorithms
- Consider memory usage
- Test with large models

## Documentation

Update relevant files:
- `README.md` - for new features
- `HOW_TO_USE.txt` - for usage instructions
- `SETUP.md` - for installation changes
- Code comments - for complex logic

## Pull Request Process

1. **Before submitting:**
   - Rebase on latest main
   - Verify tests pass
   - Check code style
   - Update documentation

2. **PR Description:**
   - Clear title
   - What changed and why
   - Screenshots (if UI changes)
   - Testing done

3. **Feedback:**
   - Address reviewer comments
   - Push updates to same branch
   - Discuss disagreements constructively

4. **Merging:**
   - Maintainer will merge when approved
   - Squash commits if requested

## Release Process

Maintainers follow semver:
- MAJOR: Breaking changes
- MINOR: New features
- PATCH: Bug fixes

## Questions?

- Check `README.md` and `HOW_TO_USE.txt`
- Open a discussion issue
- Review existing issues and PRs

## License

By contributing, you agree your code will be licensed under MIT License.

---

**Thank you for contributing!** 🎉
