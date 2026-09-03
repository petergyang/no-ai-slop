# Korean AI slop

Load this when the draft is in Korean. Everything in `SKILL.md` still applies. This file adds the slop that only shows up in Korean, plus checks to run before returning the draft.

Edit in Korean. Do not translate the draft to English and back. Keep the writer's speech level (합니다체, 해요체, 해라체, 반말) unless they ask to change it, and keep it consistent.

## Before applying anything below

**Check the register first.** Some patterns below come from persuasive Korean: posts, newsletters, announcements, marketing copy. On a 기술문서, 명세, 보고서, or 회의록, switch off exactly these six: 이분 대조, 과장된 훅, 콜론 드러내기, 단조로운 리듬, 형식 슬롭, 상투적 마무리. A spec that reads flat is doing its job. For that draft these six also override the em dash, robotic rhythm, and formatting rules in `SKILL.md` **and the matching checks in `eval.md`**: do not fail a Korean spec for its em dashes, its bold openers, or for ending every declarative in ~다, which 해라체 grammar requires. A personal 회고 or 포스트모템 is not a spec; leave all six on.

Everything else stays on. 관공서투 한자어, 사물존칭, 출처 없는 인용, filler transitions, 요약 반복 마무리 are more common in a 보고서 or 공문 than in a blog post, not less.

**Never edit inside a verbatim quote.** 인용문, 코드 블록, 서버 응답, UI 문구, 에러 메시지. A quote in 습니다체 inside a 해라체 draft is not mixed register.

**Keep product and code vocabulary.** 인덱스 최적화, 장애 대응 훈련, 결제 승인 지연. These map to code and to what the team says out loud, so they are not noun pileups or ~화 slop even when they look like one.

**Ask, never invent.** Every rule below asks for a name, number, actor, or mechanism the draft may not have. When it is missing, say so and ask the writer. Do not supply a plausible one. If honest cutting leaves a stub, hand the stub back with the question instead of padding it.

## Words and endings to cut

Empty modifiers: 다양한, 여러 가지, 수많은, 효율적인, 체계적인, 전략적인, 혁신적인, 핵심적인, 근본적인, 실질적인. Replace with the number, name, or mechanism when the draft has one. When it does not, ask, and keep the word if the plurality itself is the fact ("여러 채널에서 모았다").

Inflated claims: 게임 체인저, 판도를 바꾸는, 혁명적인, 패러다임의 전환, 새로운 지평, 필수불가결한, 바야흐로 ~의 시대. Also translated idioms: 하루가 끝날 무렵, 양날의 검, 빙산의 일각, 다음 단계로 나아갈 때, ~는 시간 문제입니다.

Hedging endings used as a default: ~라고 할 수 있습니다, ~인 것 같습니다, ~라고 볼 수 있습니다, ~할 필요가 있습니다, ~이 아닐까 싶습니다, ~것으로 보입니다. The lists in this file are written in 습니다 form; match them against the draft's own ending (~라고 볼 수 있다, ~라고 볼 수 있어요). Keep them when the writer is genuinely unsure or is leaving a decision open on purpose. Cut them when they only soften a plain claim. "이 방식이 더 빠르다고 할 수 있습니다" becomes "이 방식이 더 빠릅니다."

Filler transitions: 또한, 아울러, 뿐만 아니라, 무엇보다, 한편, 결론적으로, 정리하자면, 마지막으로. Also 문두 접속부사 repeated every sentence: 그리고, 그래서, 하지만, 따라서, 즉. Keep one when it names a real relation. Cut the rest.

관공서투 한자어: 당사, 금번, 상기, 하기와 같이, ~에 대하여, ~인 바, 제고, 인지되다, 기 언급한. Use the plain Korean word unless the document type genuinely requires the formal register.

## Patterns to cut

**번역투 (translationese).** "~에 대한", "~을 통해", "~에 있어서", "~로 인해", "~와 관련하여", "~에 기반하여", "~을 가지고 있다", "~하는 것이 가능하다", "가장 ~한 것 중 하나". These are English grammar wearing Korean. Rewrite with a Korean verb, keeping the original tense and modality. "배포 시간 단축에 대한 개선이 가능합니다" becomes "배포 시간을 줄일 수 있습니다."

**~의 남발.** Genitive stacking copied from English and Japanese. "저희 회사의 성장의 원동력의 핵심" becomes "저희 회사가 성장한 이유". Korean drops 의 far more often than English drops "of".

**과잉 존대와 사물존칭.** The loudest tell in Korean AI copy. "커피 나오셨습니다", "가격이 5만원이십니다", "확인이 필요하십니다". Objects and abstractions do not take 시. Also cut stacked 과공 표현: "말씀드리고 싶은 부분은 ~ 참고해 주시기 바랍니다."

**이중 피동 (double passive).** 보여집니다, 쓰여집니다, 잊혀집니다, 생각되어집니다. One passive marker is enough, and an active verb is usually better. "결과가 보여집니다" becomes "결과가 보입니다."

**주어 없는 피동 (agent-hiding passive).** "~이 결정되었습니다", "~이 추진되고 있습니다", "~이 도출되었습니다". Name the actor the draft already gives: "저희 팀은 기준을 다시 잡았고, 새 정책이 결정되었습니다" becomes "저희 팀은 기준을 다시 잡고 새 정책을 정했습니다." If the draft never says who, ask the writer rather than naming a plausible team. Leave the passive when the actor is named nearby, is genuinely irrelevant, or when the missing actor is itself the point ("아직 안 정해졌다").

**명사화 (noun pileups).** "품질 개선 작업 진행", "고객 만족도 향상 방안 마련", "데이터 기반 의사결정 체계 구축". Verbs are buried inside nouns and the reader has to re-parse. Unpack into a sentence. Three or more nouns before the verbal noun is the line. Table cells and product terms are exempt.

**명사구 종결.** Ending sentences with ~것이다, ~라는 점이다, ~하는 일이다, ~인 경우다. This is where Korean prose goes flabby. "이 오류가 나는 것은 캐시가 비어 있는 경우다" becomes "캐시가 비어 있으면 이 오류가 난다."

**~적, ~성, ~화 남발.** 효율적, 전략적, 확장성, 고도화, 최적화, 활성화. Each one is fine alone; stacked they say nothing, and a bulleted grid of `**확장성**: ...` labels is the same slop in list form. Keep any that is a real term in the field. Otherwise say what changed, and ask for the number if the draft lacks one.

**불필요한 대명사와 복수형.** Korean drops subjects that context supplies. Cut 그것은, 이것은, 우리는 when they carry nothing, and cut ~들 when the plural is obvious ("많은 사용자들" becomes "많은 사용자"). Keep the pronoun when it carries meaning: contrast, or the writer implicating themselves ("이 버그는 우리가 만들었다"). This rule is about empty subjects, not about stripping objects.

**한국어 이분 대조.** Only the rhetorical form: a negation split across two sentences ("X가 아닙니다. Y입니다."), a hype opener ("중요한 건 X가 아니라 Y입니다"), an escalation ("단순한 X를 넘어 Y입니다"), or a negative list ("기술의 문제가 아닙니다. 예산의 문제도 아닙니다. 사람의 문제입니다"). State Y directly. Keep "A가 아니라 B" when the negated half does work: correcting a wrong assumption the reader already holds ("이 지표는 요청 수가 아니라 세션 수를 센다"), or warning that a name misleads ("이 오류는 파일이 없다는 뜻이 아니다"). Ordinary Korean coordination is not a tic. Do not delete 아니라 on sight.

**한국어 서두 뜸들이기.** "결론부터 말하자면", "솔직히 말해서", "한 가지 분명히 하자면", "여기서 중요한 점은". Cut and state the point.

**과장된 훅과 강박 열거.** "아무도 알려주지 않는", "당신이 몰랐던 ~가지", "~의 모든 것", "이것만 알면 끝", "지금 바로 확인하세요", "~하는 사람들의 공통점", "핵심 포인트 3가지", "반드시 알아야 할 다섯 가지". Cut the setup and make the claim stand alone.

**콜론 드러내기.** "핵심은 하나입니다: 맥락이 전부입니다." Write it as a plain sentence. Colons used for an actual list, label, heading, or metadata line are fine.

**한국어 의미 부풀리기.** "~에 큰 의미를 갖습니다", "~의 중요한 이정표입니다", "시사하는 바가 큽니다", "~을 보여주는 대목입니다", "~임을 방증합니다". State the fact and let the reader judge.

**출처 없는 인용.** "전문가들은 ~라고 말합니다", "업계에서는 ~로 알려져 있습니다", "~라는 분석이 나옵니다", "연구에 따르면". Name the source or cut the claim. Ask the writer; do not invent one.

**설의법과 자문자답.** "왜일까요?", "한번 생각해 봅시다", "정답은 무엇일까요?" followed by the writer's own answer. Drop the question and make the point.

**단조로운 리듬.** Sentences that all run the same length and shape, a section where every paragraph opens with a bold claim, or 3연속 대구 ("빠르고, 정확하고, 안정적입니다"). Vary length and structure. Do not vary the speech level to do it: a 해라체 draft ends every declarative in ~다 by grammar, and that is not slop. Never mix ~죠 or ~고요 into a 합니다체 or 해라체 draft.

**상투적 마무리.** "결국 중요한 것은 사람입니다", "미래는 이미 우리 곁에 있습니다", "이제 선택은 여러분의 몫입니다", "앞으로가 더 기대됩니다". Delete the closing aphorism and end on the last concrete point or next step. A wry, concrete last line in the writer's own voice ("이번엔 운이 좋았다") is not an aphorism. Keep it.

**요약 반복 마무리.** "지금까지 ~에 대해 살펴보았습니다", "정리하자면 다음과 같습니다" followed by a restatement. The reader was just there. Cut it.

**형식 슬롭.** Emoji in headings and trailing emoji in body lines, decorative 볼드, bold on so many paragraph openers that none of them emphasizes anything, 느낌표와 물결표 남발 ("정말 놀라운 결과입니다!!", "안녕하세요~"), bullet lists where two sentences would read better, and em dashes copied from English. Korean prose rarely needs an em dash; use a comma, a period, or 괄호. 가운뎃점(·) joining coordinate nouns is standard Korean orthography, not slop.

**존대 혼용.** Mixed 합니다체 and 해요체 in the writer's own sentences, or 반말 dropped into a formal draft. Pick the writer's level and hold it. Quoted text keeps its own level.

## Eval cases

Run these after editing a Korean draft, in addition to the checks in `eval.md`.

1. 기술문서·명세·보고서라면 이분 대조, 훅, 콜론, 리듬, 형식, 상투적 마무리 여섯 가지만 껐는가? 나머지 규칙은 그대로 적용했는가?
2. 인용문, 코드, UI 문구, 에러 메시지를 그대로 두었는가?
3. 제품·코드 용어를 명사 나열이나 ~화 슬롭으로 오인해 풀어헤치지 않았는가?
4. 원문에 없던 숫자, 행위자, 출처를 지어내지 않았는가? 빠진 정보는 글쓴이에게 물었는가?
5. 번역투(~에 대한, ~을 통해, ~에 있어서, ~에 기반하여)와 ~의 남발이 한국어 문장으로 바뀌었는가?
6. 사물존칭과 과잉 존대가 사라졌는가?
7. 이중 피동이 사라졌고, 남은 피동은 행위자가 드러나거나 행위자가 중요하지 않은 경우인가?
8. 습관적인 완충 어미가 실제 불확실성이나 미결 사항을 나타낼 때만 남았는가?
9. "A가 아니라 B" 중 독자의 오해를 바로잡는 문장은 그대로 살아 있는가? 뜻을 지닌 주어(우리가, 내가)를 지우지 않았는가?
10. 종결어미를 바꾸느라 존댓말 수준이 섞이지 않았는가?
11. 요약 반복 마무리를 잘라냈는가? 설득문이라면 마지막 문장이 잠언이 아니라 구체적인 내용, 결론, 다음 행동으로 끝나는가?
