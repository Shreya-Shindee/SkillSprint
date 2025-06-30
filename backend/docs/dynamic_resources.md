# Dynamic Resource Search Feature

This feature enables SkillSprint to dynamically search and retrieve real, up-to-date learning resources for skills without requiring any API keys or paid services.

## How It Works

The dynamic resource search leverages web scraping techniques to find relevant learning materials across multiple platforms:

1. **YouTube Videos**: Searches YouTube for relevant tutorial videos about specific skills
2. **Articles and Tutorials**: Uses DuckDuckGo search to find relevant articles and tutorials
3. **GitHub Repositories**: Searches GitHub for relevant code repositories and examples

## Implementation Details

The feature is implemented in the following components:

### 1. utils/resource_search.py

Contains the core functionality for searching different platforms:

- get_youtube_videos(): Searches YouTube for videos related to a skill
- get_articles(): Searches DuckDuckGo for articles and tutorials
- get_github_repos(): Searches GitHub for relevant repositories
- get_resources_for_skill(): Combines results from all sources

### 2. ML Integration

The ml/skill_decomposition.py module has been updated to use the dynamic search functionality when recommending resources for skills.

### 3. Resource API

The /resources/by-skill-name endpoint now uses the dynamic search to provide fresh, relevant resources when a user explores a skill.

## Benefits

- **Always Fresh Content**: Resources are fetched in real-time rather than being static
- **No API Keys Required**: Works without requiring Google/YouTube API keys or other paid services
- **Diverse Resource Types**: Provides a mix of videos, articles, and code repositories
- **Fallback Mechanism**: Falls back to pre-defined resources if dynamic search fails

## Technical Notes

- The implementation uses equests and BeautifulSoup4 for web scraping
- Multiple search methods are implemented with fallbacks to ensure reliability
- Rate limiting and delays are built-in to be respectful to the services being queried
- Error handling ensures the application continues to function even if resource fetching fails

## Future Improvements

- Add more resource types (e.g., courses, podcasts, books)
- Implement caching to reduce repeated searches for popular skills
- Add filtering options to allow users to specify preferred resource types
- Improve resource ranking based on user feedback and engagement
