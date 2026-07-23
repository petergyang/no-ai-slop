# French academic evaluation cases

Run each case in a fresh context with the source passage unchanged.

## FR-EDIT-01: Formulaic academic prose

Prompt: `/no-ai-slop Révise ce paragraphe pour un article scientifique en français.`

> Dans un contexte en constante évolution, il convient de noter que la vaccination constitue un levier essentiel permettant d'optimiser la prévention. Cette dynamique met en lumière l'importance cruciale d'une démarche globale et intégrée.

Pass: removes formulaic setup and inflated abstractions; invents no mechanism, population, result, or citation; returns French prose plus `Modifications apportées`.

## FR-INTEGRITY-02: Association is not causation

Prompt: `/no-ai-slop Révise ce résultat sans modifier son degré de certitude.`

> Dans cette étude transversale, l'exposition était associée à une probabilité plus élevée de vaccination (OR ajusté : 1,42 ; IC à 95 % : 1,08–1,87). Ces résultats pourraient refléter des différences d'accès aux services, mais le devis ne permet pas d'établir une relation causale.

Pass: preserves the study design, estimate, interval, `pourraient`, and causal limitation; does not turn association into effect or causation.

## FR-CITATIONS-03: Citations and terminology

Prompt: `/no-ai-slop Révise au minimum ce passage de méthodes.`

> L'hésitation vaccinale a été définie selon le cadre du SAGE Working Group [12]. Les rapports de prévalence ajustés (RPa) et leurs intervalles de confiance à 95 % ont été estimés au moyen d'une régression de Poisson à variance robuste.

Pass: retains `SAGE Working Group [12]`, `RPa`, `95 %`, and the named model; makes few or no edits.

## FR-HUMAN-04: Strong prose remains intact

Prompt: `/no-ai-slop Révise seulement ce qui sonne artificiel.`

> Nos données ne disent pas pourquoi certaines personnes ont refusé le vaccin. Elles montrent toutefois que le refus était plus fréquent loin des centres de santé, y compris après ajustement sur l'âge et le niveau d'instruction.

Pass: leaves both sentences substantially intact and adds no explanation.

## FR-DETECT-05: Detection only

Prompt: `/no-ai-slop Détecte les formulations artificielles sans réécrire le texte.`

> Force est de constater que ces résultats marquent un tournant majeur. Ils soulignent de manière cruciale le rôle fondamental de cette approche innovante.

Pass: names patterns, quotes each affected phrase, gives short fixes, and does not rewrite, score, or infer authorship.

## FR-MIXED-06: Mixed-language routing

Prompt: `/no-ai-slop Edit this bilingual abstract without translating either language.`

> Il convient de noter que 42 % des participants étaient vaccinés. Overall, the adjusted analysis found no evidence of an association (aPR 1.03, 95% CI 0.91–1.16).

Pass: applies the matching rules to each language; preserves every number and does not translate either sentence.
