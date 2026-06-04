import gradio as gr

# Custom CSS for modern dark theme, responsive design, and professional styling
custom_css = """
:root {
    --primary: #6366f1;
    --primary-hover: #4f46e5;
    --bg-dark: #0a0a0f;
    --bg-card: #111114;
    --bg-elevated: #1a1a1f;
    --border: #2a2a2f;
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --accent: #22c55e;
    --error: #ef4444;
}

body {
    background: var(--bg-dark);
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.gradio-container {
    max-width: 1400px !important;
    margin: 0 auto !important;
    background: transparent !important;
}

/* Main app container */
.app-header {
    text-align: center;
    padding: 2rem 1rem 1.5rem 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
    background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-dark) 100%);
    border-radius: 0 0 24px 24px;
}

.app-header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #fff 0%, var(--primary) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}

.app-header p {
    color: var(--text-secondary);
    font-size: 1.1rem;
    max-width: 600px;
    margin: 0 auto;
}

/* Two-column row */
.two-columns {
    display: flex;
    gap: 1.5rem;
    padding: 0 1rem;
    flex-wrap: wrap;
}

.column {
    flex: 1;
    min-width: 280px;
}

/* Card styling */
.card {
    background: var(--bg-card);
    border-radius: 20px;
    border: 1px solid var(--border);
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 20px 40px -12px rgba(0, 0, 0, 0.5);
}

.card-header {
    padding: 1rem 1.25rem;
    background: var(--bg-elevated);
    border-bottom: 1px solid var(--border);
    font-weight: 600;
    font-size: 1.1rem;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.card-content {
    padding: 1.25rem;
}

/* Textbox styling */
textarea, input {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    font-size: 0.95rem !important;
    padding: 0.75rem !important;
    transition: all 0.2s ease !important;
}

textarea:focus, input:focus {
    border-color: var(--primary) !important;
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2) !important;
}

/* Button styling */
.analyze-btn {
    background: linear-gradient(135deg, var(--primary) 0%, #818cf8 100%) !important;
    border: none !important;
    border-radius: 40px !important;
    padding: 0.9rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    color: white !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
    margin: 1rem 0 !important;
    box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.4) !important;
}

.analyze-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px 0 rgba(99, 102, 241, 0.5) !important;
    filter: brightness(1.05);
}

/* Results markdown area */
.results-area {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 0.5rem !important;
}

.results-area .prose {
    max-width: 100%;
}

.results-area code {
    background: var(--bg-dark);
    padding: 0.2rem 0.4rem;
    border-radius: 6px;
    font-size: 0.85rem;
}

/* Footer */
.footer {
    text-align: center;
    padding: 2rem 1rem;
    margin-top: 2rem;
    border-top: 1px solid var(--border);
    color: var(--text-secondary);
    font-size: 0.85rem;
}

/* Gradio overrides */
.gradio-row {
    gap: 0 !important;
}

label {
    color: var(--text-secondary) !important;
    font-weight: 500 !important;
}

/* Responsive */
@media (max-width: 768px) {
    .two-columns {
        flex-direction: column;
        gap: 1rem;
    }
    
    .app-header h1 {
        font-size: 1.8rem;
    }
    
    .card-header {
        padding: 0.75rem 1rem;
    }
    
    .card-content {
        padding: 1rem;
    }
}
"""

def analyze_resume(resume_text: str, job_description: str) -> str:
    """
    Core analysis function that evaluates resume against job description.
    In a real implementation, this would use AI/ML for scoring.
    """
    if not resume_text or not resume_text.strip():
        return "⚠️ **Error**: Please paste your resume content."
    
    if not job_description or not job_description.strip():
        return "⚠️ **Error**: Please paste the job description."
    
    # Simple heuristic analysis (replace with actual AI in production)
    resume_lower = resume_text.lower()
    job_lower = job_description.lower()
    
    # Keyword extraction simulation
    common_keywords = []
    job_words = set(job_lower.split())
    resume_words = set(resume_lower.split())
    
    # Simple keyword overlap (simplified for demo)
    keywords = ["python", "java", "javascript", "react", "sql", "aws", "docker", 
                "kubernetes", "tensorflow", "pytorch", "machine learning", "ai",
                "leadership", "project management", "agile", "scrum", "communication"]
    
    matched = [kw for kw in keywords if kw in resume_lower and kw in job_lower]
    
    # Calculate match score
    if len(matched) > 0:
        score = min(95, 50 + len(matched) * 5)
    else:
        score = 35
    
    # Generate markdown report
    report = f"""
<div style="background: linear-gradient(135deg, #1a1a1f 0%, #111114 100%); padding: 1.5rem; border-radius: 16px;">
    
### 🎯 Match Score: {score}%

<div style="background: #2a2a2f; border-radius: 12px; height: 8px; margin: 1rem 0;">
    <div style="background: linear-gradient(90deg, #6366f1, #22c55e); width: {score}%; height: 8px; border-radius: 12px;"></div>
</div>

---

### 📊 Analysis Summary

| Metric | Result |
|--------|--------|
| **Keyword Matches** | {len(matched)}/{len([kw for kw in keywords if kw in job_lower])} |
| **Technical Fit** | {"Excellent" if score > 80 else "Good" if score > 60 else "Needs Improvement"} |
| **Recommended Action** | {"Proceed to Interview" if score > 70 else "Customize Resume"} |

---

### 🔑 Matched Keywords
{', '.join(f"`{kw}`" for kw in matched) if matched else "*No significant keyword matches found*"}

### 💡 Recommendations

{"✅ Your resume aligns well with this role. Focus on highlighting the matched skills in your interview." if score > 70 else "⚠️ Consider adding the missing keywords from the job description to improve ATS scoring."}

### 📝 Detailed Notes

- **Strengths**: {"Strong keyword alignment" if matched else "Resume needs more role-specific terminology"}
- **Gap Analysis**: {"Add 2-3 bullet points addressing the missing skills above" if score < 80 else "Minor formatting improvements could help"}
- **ATS Compatibility**: {"Good" if score > 60 else "Consider simplifying formatting"}

---

*🤖 AI analysis based on keyword matching and job description alignment. For production use, integrate with OpenAI API or similar for semantic matching.*

</div>
"""
    return report


# Build the Gradio Blocks UI
with gr.Blocks(
    title="AI Resume & Job Match Analyzer",
    theme=gr.themes.Soft(primary_hue="indigo", neutral_hue="gray"),
    css=custom_css,
    elem_id="app-container"
) as demo:
    
    # Header section
    gr.HTML("""
    <div class="app-header">
        <h1>✨ AI Resume & Job Match Analyzer</h1>
        <p>Intelligent resume-job matching powered by artificial intelligence</p>
    </div>
    """)
    
    # Two-column layout
    with gr.Row(elem_classes="two-columns"):
        
        # Left column - Resume input
        with gr.Column(elem_classes="column"):
            with gr.Group(elem_classes="card"):
                with gr.Row(elem_classes="card-header"):
                    gr.HTML("📄 <span>Resume</span>")
                with gr.Row(elem_classes="card-content"):
                    resume_input = gr.Textbox(
                        label="Paste your resume content",
                        placeholder="Paste your resume text here...\n\nExample:\nSenior Software Engineer with 5+ years of experience in Python, AWS, and React...",
                        lines=15,
                        max_lines=25,
                        elem_id="resume-textbox"
                    )
        
        # Right column - Job description input
        with gr.Column(elem_classes="column"):
            with gr.Group(elem_classes="card"):
                with gr.Row(elem_classes="card-header"):
                    gr.HTML("💼 <span>Job Description</span>")
                with gr.Row(elem_classes="card-content"):
                    job_input = gr.Textbox(
                        label="Paste the job description",
                        placeholder="Paste the job posting here...\n\nExample:\nWe are looking for a Senior Software Engineer proficient in Python, cloud technologies...",
                        lines=15,
                        max_lines=25,
                        elem_id="job-textbox"
                    )
    
    # Analyze button row
    with gr.Row():
        analyze_btn = gr.Button(
            "🔍 Analyze Match",
            variant="primary",
            size="lg",
            elem_classes="analyze-btn"
        )
    
    # Results section
    with gr.Row():
        with gr.Column():
            with gr.Group(elem_classes="card"):
                with gr.Row(elem_classes="card-header"):
                    gr.HTML("📊 <span>Analysis Results</span>")
                with gr.Row(elem_classes="card-content"):
                    output_md = gr.Markdown(
                        value="✨ **Ready to analyze** — Paste your resume and job description, then click 'Analyze Match'.",
                        elem_classes="results-area",
                        line_breaks=True
                    )
    
    # Footer
    gr.HTML("""
    <div class="footer">
        <p>🔒 Your data is processed locally and never stored | AI Resume & Job Match Analyzer v1.0</p>
        <p style="margin-top: 0.5rem;">⚡ Built by Fatima Arif | AI/ML Enthusiast | LLM & AI Integration</p>
    </div>
    """)
    
    # Wire up the analyze button
    analyze_btn.click(
        fn=analyze_resume,
        inputs=[resume_input, job_input],
        outputs=output_md
    )
    
    # Add example placeholders (optional helper text)
    gr.HTML("""
    <div style="padding: 0 1rem; margin-top: 0.5rem;">
        <p style="color: #64748b; font-size: 0.8rem;">💡 <strong>Pro tip:</strong> For best results, use a plain-text version of your resume and include the full job description.</p>
    </div>
    """)

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)