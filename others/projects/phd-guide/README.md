# PhD Project Guide — Reusable Backbone

Use this flow when creating a standalone HTML study guide for another PhD project.

## Request

Ask:

> Read `phd-guide/README.md` and use its flow to build a similar standalone HTML guide for this PhD project: [project description or source link].

Provide the project advert, papers, notes, or existing guide that should be used as source material.

## Guide structure

Build one self-contained HTML file with these sections:

1. **Project overview and research question**
   - Explain the project in plain language.
   - State the central research question and intended outcome.

2. **Domain knowledge and key terms**
   - Introduce the biology, technology, or theory needed to understand the project.
   - Define unfamiliar terms where they first appear.

3. **Research idea, hypotheses, and novelty**
   - Explain the proposed idea and why it may work.
   - Separate established evidence from inference and open research questions.

4. **Work packages and complete workflow**
   - Present the full project from initial inputs to final validation.
   - For every step record: input, action, tools, output, decision gate, common failure, and return path.

5. **Validation plan and success measures**
   - Show how each important claim will be tested.
   - Include positive, negative, specificity, abundance, and technical controls where relevant.

6. **Evidence, risks, limits, and failure paths**
   - Summarise the strongest supporting evidence.
   - Explain realistic failure modes and how each result changes the next step.

7. **Tools, automation, and human decisions**
   - Identify tasks suitable for scripting or automation.
   - Identify decisions that require expert judgement.
   - Preserve parameters, versions, inputs, outputs, and provenance.

8. **Applicant preparation**
   - Describe useful existing skills and likely skill gaps.
   - Add relevant interview questions.

9. **Reference material**
   - Include a glossary, key papers, software documentation, and project sources.

## Content rules

- Store each detailed fact in one place; refer to it elsewhere instead of repeating it.
- Keep one complete workflow rather than separate overlapping summaries.
- Keep concepts and decision logic in the main guide.
- Put long commands, exercises, and tutorials in a separate appendix only when requested.
- Remove hidden legacy sections and duplicate diagrams.
- Distinguish published evidence, reasonable inference, and untested hypotheses.
- Do not present predictions, model scores, or visual plausibility as experimental proof.
- Explain what success and failure look like at every major gate.

## HTML requirements

- Produce one standalone HTML file with embedded CSS and JavaScript.
- Preserve the visual style of `syntheticprotein.html` unless another design is requested.
- Include sidebar navigation, search, clear-search, expandable details, and print/PDF support.
- Make tables horizontally scrollable on small screens.
- Use semantic headings, keyboard-accessible controls, descriptive links, and meaningful image alt text.
- Open external links safely with `target="_blank"` and `rel="noopener"`.
- Ensure the file works when opened directly without a build system or web server.

## Final checks

- Confirm every section is reachable from navigation.
- Test search, clear-search, expandable details, and external links.
- Check desktop and mobile layouts for clipping or overflow.
- Confirm tables remain readable on narrow screens.
- Confirm all useful content appears in print/PDF output.
- Confirm the source file was not changed unless explicitly requested.
