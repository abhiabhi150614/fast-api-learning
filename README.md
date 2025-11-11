# 🎓 EduAI - Next-Generation AI Learning & Recruitment Ecosystem

<div align="center">

![Platform](https://img.shields.io/badge/EduAI-Dual%20Platform-blue?style=for-the-badge)
![AI](https://img.shields.io/badge/Gemini-2.0%20Flash-green?style=for-the-badge)
![OAuth](https://img.shields.io/badge/Composio-8%20Services-purple?style=for-the-badge)
![Voice](https://img.shields.io/badge/Twilio-Voice%20AI-red?style=for-the-badge)
![Components](https://img.shields.io/badge/React-43%20Components-61DAFB?style=for-the-badge&logo=react)
![Backend](https://img.shields.io/badge/FastAPI-11%20Modules-009688?style=for-the-badge&logo=fastapi)

**Revolutionary AI-powered dual-platform bridging personalized education with intelligent talent acquisition**

[Architecture](#-system-architecture) • [Features](#-core-capabilities) • [Tech Stack](#-technology-ecosystem) • [Installation](#-quick-start) • [API](#-api-reference)

</div>

---

## 🌟 Platform Overview

EduAI is a comprehensive dual-user ecosystem that revolutionizes both learning and recruitment through advanced AI integration:

- **For Students**: AI-generated personalized learning paths with 30-day monthly structures, adaptive quizzes, voice tutoring, and automated progress tracking
- **For Recruiters**: Intelligent candidate matching, AI-powered email analysis, automated interview scheduling, and comprehensive talent analytics

**Built in 6 days** | **43 React Components** | **11 Backend Modules** | **15 Database Models** | **8 OAuth Integrations**

---

## 🏛️ System Architecture

### High-Level Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        WEB[Web Application<br/>React 19.1.0<br/>43 Components]
        MOBILE[Progressive Web App<br/>Offline Capable]
    end
    
    subgraph "API Gateway Layer"
        FASTAPI[FastAPI Server<br/>11 Route Modules<br/>JWT Auth]
        FLASK[Flask Call Server<br/>Twilio Webhooks<br/>Voice AI]
    end
    
    subgraph "AI & Intelligence Layer"
        GEMINI[Gemini 2.0 Flash<br/>4-Model Fallback<br/>Function Calling]
        CONTEXT[Context Manager<br/>Session Storage<br/>History Tracking]
        TOOLS[8 Function Tools<br/>Drive, YouTube, LinkedIn<br/>GitHub, Twitter, Calls]
    end
    
    subgraph "Integration Layer"
        COMPOSIO[Composio OAuth<br/>8 Individual Services<br/>Consistent API]
        GOOGLE[Google Services<br/>Drive, Gmail, Calendar<br/>Meet, YouTube]
        TWILIO[Twilio Voice<br/>Speech Recognition<br/>TwiML Responses]
    end
    
    subgraph "Data Layer"
        POSTGRES[(PostgreSQL<br/>15 Models<br/>JSONB Support)]
        VECTOR[Vector Store<br/>Candidate Embeddings<br/>Similarity Search]
    end
    
    subgraph "Background Services"
        GITHUB_WORKER[GitHub Worker<br/>Repo Creation<br/>Daily Commits]
        EMAIL_WORKER[Email Worker<br/>Notifications<br/>HTML Templates]
        ANALYTICS[Analytics Engine<br/>Progress Tracking<br/>Performance Metrics]
    end
    
    WEB --> FASTAPI
    MOBILE --> FASTAPI
    WEB --> FLASK
    
    FASTAPI --> GEMINI
    FASTAPI --> COMPOSIO
    FASTAPI --> POSTGRES
    
    FLASK --> GEMINI
    FLASK --> TWILIO
    
    GEMINI --> CONTEXT
    GEMINI --> TOOLS
    
    COMPOSIO --> GOOGLE
    
    TOOLS --> GOOGLE
    TOOLS --> COMPOSIO
    
    FASTAPI --> GITHUB_WORKER
    FASTAPI --> EMAIL_WORKER
    FASTAPI --> ANALYTICS
    
    GITHUB_WORKER --> COMPOSIO
    EMAIL_WORKER --> GOOGLE
    ANALYTICS --> POSTGRES
    ANALYTICS --> VECTOR
    
    style GEMINI fill:#4CAF50
    style COMPOSIO fill:#9C27B0
    style POSTGRES fill:#336791
    style FASTAPI fill:#009688
    style FLASK fill:#000000
```


### Detailed Component Architecture

```mermaid
graph LR
    subgraph "Frontend - 43 Components"
        subgraph "Student UI - 25 Components"
            S1[Dashboard & Landing]
            S2[Auth & Onboarding]
            S3[Learning Plans & Progress]
            S4[Quiz System]
            S5[AI Chatbot]
            S6[Voice Tutor]
            S7[Social Connections]
            S8[Calendar & Notes]
        end
        
        subgraph "Recruiter UI - 18 Components"
            R1[Dashboard & Analytics]
            R2[Candidate Management]
            R3[Job Postings]
            R4[Email Analysis]
            R5[Interview Scheduler]
            R6[AI Assistant]
            R7[Shortlist Manager]
        end
    end
    
    subgraph "Backend - 11 Route Modules"
        B1[auth.py<br/>JWT + OAuth]
        B2[onboarding.py<br/>Profile Setup]
        B3[learning_plan.py<br/>AI Plan Generation]
        B4[subplans.py<br/>Month Management]
        B5[quiz.py<br/>Quiz Engine]
        B6[chatbot.py<br/>AI Chat + Tools]
        B7[call_bot.py<br/>Voice Integration]
        B8[voice_webhook.py<br/>Twilio Handlers]
        B9[recruiter.py<br/>Recruitment Suite]
        B10[recruit.py<br/>Matching Engine]
        B11[youtube_schedule.py<br/>Video Management]
    end
    
    S1 --> B1
    S2 --> B2
    S3 --> B3
    S3 --> B4
    S4 --> B5
    S5 --> B6
    S6 --> B7
    S6 --> B8
    S8 --> B11
    
    R1 --> B9
    R2 --> B9
    R3 --> B9
    R4 --> B9
    R5 --> B9
    R6 --> B9
    R7 --> B10
    
    style S5 fill:#4CAF50
    style S6 fill:#FF5722
    style R6 fill:#2196F3
    style B6 fill:#4CAF50
    style B9 fill:#FF9800
```


### Data Flow Architecture

```mermaid
sequenceDiagram
    participant Student
    participant React
    participant FastAPI
    participant Gemini
    participant Composio
    participant Google
    participant PostgreSQL
    
    Note over Student,PostgreSQL: Learning Plan Generation Flow
    
    Student->>React: Request Learning Plan
    React->>FastAPI: POST /learning-plan/generate
    FastAPI->>PostgreSQL: Get Onboarding Data
    PostgreSQL-->>FastAPI: User Profile
    FastAPI->>Gemini: Generate Plan Structure
    Gemini-->>FastAPI: 12-36 Months Plan
    FastAPI->>PostgreSQL: Save Learning Plan
    FastAPI->>Gemini: Generate Month 1 (30 Days)
    Gemini-->>FastAPI: Daily Concepts
    FastAPI->>Gemini: Generate Day 1 Detail
    Gemini-->>FastAPI: Sections + Resources
    FastAPI->>Gemini: Generate Day 1 Quiz
    Gemini-->>FastAPI: 15 Questions
    FastAPI->>Composio: Create Drive Folders
    Composio->>Google: EDUAI_NAME_LEARNING_MAIN_PATH
    Google-->>Composio: Folder Created
    FastAPI->>PostgreSQL: Save Complete Plan
    FastAPI-->>React: Learning Plan Ready
    React-->>Student: Display Plan
    
    Note over Student,PostgreSQL: Quiz Submission & Progression Flow
    
    Student->>React: Submit Quiz Answers
    React->>FastAPI: POST /quiz/submit
    FastAPI->>PostgreSQL: Get Quiz & Submissions
    FastAPI->>FastAPI: Calculate Score
    
    alt Score >= 70%
        FastAPI->>PostgreSQL: Mark Day Complete
        FastAPI->>Composio: Send Gmail Notification
        Composio->>Google: Success Email
        FastAPI->>PostgreSQL: Check Month Status
        
        alt Month Complete
            FastAPI->>Gemini: Generate Next Month
            Gemini-->>FastAPI: 30 New Days
            FastAPI->>PostgreSQL: Activate Next Month
        end
        
        FastAPI-->>React: Success + Next Day
    else Score < 70%
        FastAPI->>PostgreSQL: Save Failed Attempt
        
        alt Attempts >= 2
            FastAPI->>Gemini: Regenerate Content
            Gemini-->>FastAPI: Enhanced Material
            FastAPI->>PostgreSQL: Update Day Detail
        end
        
        FastAPI-->>React: Retry Required
    end
    
    React-->>Student: Show Results
```


### AI Integration Architecture

```mermaid
graph TB
    subgraph "AI Function Calling System"
        USER[User Query]
        CHATBOT[AI Chatbot<br/>Context-Aware]
        GEMINI[Gemini 2.0 Flash<br/>Function Calling API]
        
        subgraph "8 Function Tools"
            T1[get_drive_notes<br/>Retrieve Notes]
            T2[update_drive_notes<br/>Save Content]
            T3[search_youtube_videos<br/>Find Videos]
            T4[create_youtube_playlist<br/>New Playlist]
            T5[add_video_to_playlist<br/>Add Video]
            T6[initiate_call<br/>Voice Call]
            T7[create_linkedin_post<br/>Social Post]
            T8[context_query<br/>Learning Position]
        end
        
        subgraph "Service Integrations"
            DRIVE[Google Drive API]
            YOUTUBE[YouTube Data API]
            LINKEDIN[LinkedIn via Composio]
            TWILIO[Twilio Voice API]
        end
    end
    
    USER --> CHATBOT
    CHATBOT --> GEMINI
    GEMINI --> T1
    GEMINI --> T2
    GEMINI --> T3
    GEMINI --> T4
    GEMINI --> T5
    GEMINI --> T6
    GEMINI --> T7
    GEMINI --> T8
    
    T1 --> DRIVE
    T2 --> DRIVE
    T3 --> YOUTUBE
    T4 --> YOUTUBE
    T5 --> YOUTUBE
    T6 --> TWILIO
    T7 --> LINKEDIN
    
    DRIVE --> GEMINI
    YOUTUBE --> GEMINI
    LINKEDIN --> GEMINI
    TWILIO --> GEMINI
    
    GEMINI --> CHATBOT
    CHATBOT --> USER
    
    style GEMINI fill:#4CAF50
    style CHATBOT fill:#2196F3
    style USER fill:#FF9800
```


### Recruiter Intelligence Architecture

```mermaid
graph TB
    subgraph "Recruiter Platform Intelligence"
        RECRUITER[Recruiter Dashboard]
        
        subgraph "AI Matching Engine"
            MATCH[Candidate Matcher<br/>Multi-Factor Analysis]
            SCORE[Scoring Algorithm<br/>0-100 Scale]
            EXPLAIN[Match Explanation<br/>AI Generated]
        end
        
        subgraph "Email Intelligence"
            FETCH[Gmail Fetcher<br/>Job Emails]
            PARSE[PDF Parser<br/>Resume Extraction]
            SUMMARIZE[AI Summarizer<br/>Structured Format]
            SKILLS[Skill Extractor<br/>NLP Based]
        end
        
        subgraph "Interview Automation"
            CALENDAR[Calendar Checker<br/>Availability]
            MEET[Google Meet<br/>Link Generator]
            INVITE[Email Inviter<br/>Auto Send]
            TRACK[Lifecycle Tracker<br/>Status Management]
        end
        
        subgraph "Data Sources"
            STUDENTS[(Student Profiles<br/>Learning Data)]
            QUIZZES[(Quiz Scores<br/>Performance)]
            SOCIAL[(Social Connections<br/>LinkedIn, GitHub)]
            EMAILS[(Email Applications<br/>Resumes)]
        end
    end
    
    RECRUITER --> MATCH
    RECRUITER --> FETCH
    RECRUITER --> CALENDAR
    
    MATCH --> STUDENTS
    MATCH --> QUIZZES
    MATCH --> SOCIAL
    MATCH --> SCORE
    SCORE --> EXPLAIN
    
    FETCH --> EMAILS
    FETCH --> PARSE
    PARSE --> SUMMARIZE
    SUMMARIZE --> SKILLS
    
    CALENDAR --> MEET
    MEET --> INVITE
    INVITE --> TRACK
    
    EXPLAIN --> RECRUITER
    SKILLS --> RECRUITER
    TRACK --> RECRUITER
    
    style MATCH fill:#FF5722
    style SUMMARIZE fill:#4CAF50
    style MEET fill:#2196F3
```

---

## 🎯 Core Capabilities

### 📚 Student Learning Platform

#### 1. AI-Powered Personalized Learning Plans

**Intelligent Curriculum Generation:**
- Gemini 2.0 analyzes career goals, current skills, education level, and time commitment
- Generates 1-3 year learning journeys (12-36 months)
- Each month contains 30 detailed daily learning objectives
- Sequential progression with 70% quiz pass requirement
- Adaptive content that evolves based on performance

**Technical Implementation:**
```python
# Plan Generation Pipeline
def generate_learning_plan(user_id):
    onboarding = get_onboarding_data(user_id)
    total_years = decide_years(onboarding.grade)  # 1-3 years
    
    # AI generates month structure
    plan_structure = gemini.generate_content(
        prompt=build_plan_prompt(onboarding, total_years)
    )
    
    # Generate 30 days for first month
    month_1_days = _generate_days_for_month_via_ai(
        month=plan_structure.months[0],
        onboarding=onboarding
    )
    
    # Generate detailed content for day 1
    day_1_detail = _generate_day_detail_via_ai(
        month=plan_structure.months[0],
        day=month_1_days[0],
        onboarding=onboarding
    )
    
    # Auto-generate quiz for day 1
    day_1_quiz = _generate_quiz_via_ai(
        month=plan_structure.months[0],
        day=month_1_days[0],
        onboarding=onboarding,
        num_questions=15
    )
    
    # Create Google Drive folder structure
    create_drive_structure(user_id, onboarding.name)
    
    return complete_plan
```

**Day Detail Structure:**
- **Overview**: Comprehensive description of learning objectives
- **Sections**: Time-boxed study segments (Theory, Practice, Review)
- **Resources**: Curated documentation, videos, articles
- **Checklist**: Concrete tasks to complete
- **Learning Objectives**: Specific measurable outcomes

