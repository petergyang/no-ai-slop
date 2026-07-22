# Pattern examples

This gallery shows one before/after edit for every pattern in `SKILL.md`. Use the fixture at the end to check whether detect mode returns the expected findings without rewriting the sample.

## Words to cut

Before: It's worth noting that this robust tool streamlines invoice review.

After: The tool makes invoice review faster.

Rule: Cut banned words and empty phrases.

## Patterns to cut

### Binary contrasts

Before: The question isn't the model. It's the eval.

After: The eval matters more than the model.

Rule: State the second point directly.

### Throat-clearing openers

Before: I'll be honest, the pricing page is confusing.

After: The pricing page is confusing.

Rule: Cut the opener and state the point.

### Faux-insight setups

Before: The part everyone misses: distribution is the real moat.

After: Distribution is the moat.

Rule: Cut the setup and let the claim stand.

### Colon reveals

Before: The detail that makes it work: a separate agent grades it.

After: A separate agent does the grading, which is what makes it work.

Rule: Rewrite fake reveals as plain sentences.

### Superficial analysis

Before: The launch adds file search, highlighting the team's commitment to better workflows.

After: The launch adds file search, so users can find old drafts without leaving the editor.

Rule: Replace fake analysis with a concrete effect.

### Importance puffery

Before: The launch marks a pivotal moment for the company.

After: The launch is the company's first paid product.

Rule: State the fact and let the reader judge.

### Weasel attribution

Before: Experts agree that short forms improve completion rates.

After: Our May usability test found that 18 of 20 people finished the short form.

Rule: Name the source or cut the claim.

### Fake-strong verbs

Before: The app serves as a centralized hub for sponsor management.

After: The app tracks sponsors, drafts, due dates, and approvals in one place.

Rule: Prefer direct verbs, including is and has.

### Synonym cycling

Before: The agent reviews the draft. The assistant scores the piece. The tool suggests fixes.

After: The agent reviews the draft, scores it, and suggests fixes.

Rule: Repeat the clear word instead of rotating terms.

### Negative listing

Before: Not a dashboard. Not a report. A daily list of overdue invoices.

After: It is a daily list of overdue invoices.

Rule: Say the positive point directly.

### Dramatic fragmentation

Before: That's it. That's the whole thing.

After: That is the whole process.

Rule: Use complete sentences.

### Robotic rhythm

Before: We collect feedback. We sort feedback. We share feedback.

After: We collect and sort feedback, then share it with the product team.

Rule: Vary sentence shape only when it helps.

### Rhetorical setups

Before: What if I told you the fix takes five minutes?

After: The fix takes five minutes.

Rule: Drop the setup and make the point.

### Fake-profound kickers

Before: The team will review the pilot results Friday. The roadmap is a compass, but courage chooses the road.

After: The team will review the pilot results Friday.

Rule: Delete the kicker and end on a concrete sentence.

### Summary-recap endings

Before: The beta opens Friday. In conclusion, this release gives teams a better way to plan.

After: The beta opens Friday.

Rule: End on a concrete point or next action.

### Formatting slop

Before: `## 🚀 Faster reviews`

After: `## Faster reviews`

Rule: Let the content determine the formatting.

### Em dashes

Before: The export is ready — after three retries — for download.

After: After three retries, the export is ready for download.

Rule: Use clearer punctuation when a dash adds nothing.

## Try detect mode

```
Here's the thing, this release changes how teams handle support requests. The old queue mixed bug reports, billing questions, and account changes in one view, so agents spent time sorting work before they could answer it. This is not a cosmetic refresh. It's a faster way to route each request to the right person. The best part: it learns which queue each customer uses most often. The launch marks a pivotal moment for our support product. Experts agree that faster routing improves customer trust. Teams can now set rules by account, topic, and urgency, then review every automatic assignment in the activity log. We will measure median response time for four weeks and publish the result. In conclusion, this update makes support work easier and more efficient.
```

### Expected findings

1. Throat-clearing openers: "Here's the thing, this release changes how teams handle support requests." Fix: Cut the opener and state the point.
2. Binary contrasts: "This is not a cosmetic refresh. It's a faster way to route each request to the right person." Fix: State the faster routing directly.
3. Colon reveals: "The best part: it learns which queue each customer uses most often." Fix: Rewrite it as a plain sentence.
4. Importance puffery: "The launch marks a pivotal moment for our support product." Fix: State what makes the launch new.
5. Weasel attribution: "Experts agree that faster routing improves customer trust." Fix: Name the source or cut the claim.
6. Summary-recap endings: "In conclusion, this update makes support work easier and more efficient." Fix: End on the measurement plan.

Paste the paragraph after `/no-ai-slop is this AI slop?` and compare the response with these findings.
