# TOBE MCP Server

A comprehensive Python MCP (Model Context Protocol) server providing specialized AI-powered tools and prompts to improve development efficiency, content creation, and learning experiences.

## 🌟 Features

### 🤖 **Developer Assistant**
- **Software System Design**: Comprehensive system architecture and implementation guidance
- **Code Review**: Detailed code analysis with actionable feedback
- **Development Best Practices**: Clean code principles and optimization strategies

### 🎨 **UI/UX Designer**
- **UI Design Prototypes**: Complete design solutions with detailed specifications
- **Design Systems**: Comprehensive design tokens and component libraries
- **Accessibility Audits**: WCAG compliance and inclusive design guidance
- **DRD Generation**: Detailed design requirement documents for developers

### 📚 **English Teacher**
- **Word Lessons**: Detailed vocabulary explanations with pronunciation and usage
- **Vocabulary Builder**: Thematic word lists and learning activities
- **Grammar Explanations**: Comprehensive grammar lessons with examples
- **Conversation Practice**: Interactive dialogue scenarios and role-play
- **Reading Comprehension**: Educational reading materials with questions
- **Pronunciation Guide**: Sound analysis and practice exercises

### ✍️ **Article Writer**
- **Article Generation**: Complete articles in English and Chinese
- **Content Outlines**: Strategic content planning and structure
- **Article Editing**: Content improvement and optimization
- **Multilingual Content**: Cultural adaptation and localization
- **SEO Optimization**: Search engine optimization and keyword analysis
- **Content Analysis**: Quality assessment and performance evaluation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tobe-mcp
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Run the server**
   ```bash
   tobe-mcp
   ```

### Development Setup

1. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

2. **Run tests**
   ```bash
   pytest
   ```

3. **Format code**
   ```bash
   black src/
   isort src/
   ```

## 📖 Usage

### Developer Prompts

#### System Design
```bash
/tobe-mcp/design "Create a web application for task management with user authentication"
```

#### Code Review
```bash
/tobe-mcp/review
# Paste your code or provide a link to review
```

### UI/UX Design Prompts

#### UI Design
```bash
/tobe-mcp/UIdesign "Design a mobile app interface for food delivery with dark mode support"
```

#### Design System
```bash
/tobe-mcp/design_system "E-commerce Platform" "Modern, clean, accessible design"
```

#### Accessibility Audit
```bash
/tobe-mcp/accessibility_audit "Review the accessibility of our login form design"
```

### English Learning Prompts

#### Word Lesson
```bash
/tobe-mcp/word_lesson "serendipity" "Advanced vocabulary for creative writing"
```

#### Vocabulary Builder
```bash
/tobe-mcp/vocabulary_builder "Technology" "intermediate" 15
```

#### Grammar Explanation
```bash
/tobe-mcp/grammar_explanation "Present Perfect Tense" "intermediate"
```

#### Conversation Practice
```bash
/tobe-mcp/conversation_practice "Job Interview" "intermediate" 2
```

#### Reading Comprehension
```bash
/tobe-mcp/reading_comprehension "Climate Change" "intermediate" "medium"
```

#### Pronunciation Guide
```bash
/tobe-mcp/pronunciation_guide "th sounds" "intermediate"
```

### Article Writing Prompts

#### Article Generation
```bash
/tobe-mcp/article_generator "The Future of Artificial Intelligence in Healthcare" "english" "blog" "professionals" 1200
```

#### Content Outline
```bash
/tobe-mcp/content_outline "Sustainable Living Practices" "article" "long" "environmentalists"
```

#### Article Editing
```bash
/tobe-mcp/article_editor "Your article content here" "seo" "general"
```

#### Multilingual Content
```bash
/tobe-mcp/multilingual_content "Original English content" "chinese" "Chinese business culture"
```

#### SEO Optimization
```bash
/tobe-mcp/seo_optimization "Your content here" "digital marketing tips" "blog"
```

#### Content Analysis
```bash
/tobe-mcp/content_analysis "Your content here" "comprehensive"
```

## 🏗️ Project Structure

```
tobe-mcp/
├── src/
│   ├── prompts/
│   │   ├── developer.py          # Software development prompts
│   │   ├── ui_designer.py        # UI/UX design prompts
│   │   ├── english_teacher.py    # English learning prompts
│   │   └── article_writer.py     # Content creation prompts
│   ├── tools/                    # Additional tools (future)
│   ├── logger.py                 # Centralized logging system
│   └── server.py                 # Main MCP server
├── docs/                         # Documentation
├── logs/                         # Application logs
├── tests/                        # Test files
├── pyproject.toml               # Project configuration
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies
└── setup.py                     # Package setup
```

## 🔧 Configuration

### Logging

The server uses a centralized logging system with configurable levels:

```python
from src.logger import get_logger

logger = get_logger("your_module_name")
logger.info("Your log message")
```

### Environment Variables

- `LOG_LEVEL`: Set logging level (DEBUG, INFO, WARNING, ERROR)
- `LOG_FILE`: Specify custom log file path

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_server.py
```

## 📝 Development

### Adding New Prompts

1. Create a new prompt file in `src/prompts/`
2. Follow the existing pattern:
   ```python
   from mcp.server.fastmcp import FastMCP
   from src.logger import get_logger

   def your_prompt_function(mcp: FastMCP):
       logger = get_logger("your_prompt_name")
       
       @mcp.prompt("your_prompt_name")
       def your_prompt(param: str) -> str:
           logger.info(f"Processing: {param}")
           print(f"Processing: {param}")
           return f"Your prompt response for: {param}"
   ```

3. Register the prompt in `src/server.py`

### Code Style

- Use Black for code formatting
- Use isort for import sorting
- Follow PEP 8 guidelines
- Add type hints where appropriate

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Write tests for new features
- Update documentation as needed
- Follow the existing code patterns
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)
- Powered by FastMCP framework
- Inspired by the need for efficient AI-powered development tools

## 📞 Support

For questions, issues, or contributions:

- Open an issue on GitHub
- Check the documentation in the `docs/` directory
- Review the test examples for usage patterns

---

**Made with ❤️ by the TOBE Team** 