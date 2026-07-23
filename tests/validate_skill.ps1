$ErrorActionPreference = 'Stop'

function Assert-Contains {
    param([string]$Path, [string]$Pattern)
    $content = Get-Content -Raw -LiteralPath $Path
    if ($content -notmatch $Pattern) {
        throw "Expected '$Path' to match: $Pattern"
    }
}

$requiredFiles = @(
    'references/english.md',
    'references/french-academic.md',
    'tests/french-academic-cases.md'
)

foreach ($path in $requiredFiles) {
    if (-not (Test-Path -LiteralPath $path)) {
        throw "Missing required file: $path"
    }
}

Assert-Contains 'SKILL.md' '## Language routing'
Assert-Contains 'SKILL.md' 'French academic and research writing'
Assert-Contains 'SKILL.md' 'references/english\.md'
Assert-Contains 'SKILL.md' 'references/french-academic\.md'
Assert-Contains 'SKILL.md' 'Do not translate unless the user explicitly asks'
Assert-Contains 'references/english.md' 'Binary contrasts'
Assert-Contains 'references/french-academic.md' '## Intégrité scientifique'
Assert-Contains 'references/french-academic.md' 'Modifications apportées'
Assert-Contains 'references/french-academic.md' 'Ne pas transformer une association en effet ou en causalité'
Assert-Contains 'eval.md' '## French academic and research writing'
Assert-Contains 'eval.md' 'association and causation'
Assert-Contains 'README.md' 'French academic and research writing'
Assert-Contains 'agents/openai.yaml' 'French academic'

$caseCount = (Select-String -Path 'tests/french-academic-cases.md' -Pattern '^## FR-' -AllMatches).Count
if ($caseCount -ne 6) {
    throw "Expected 6 French evaluation cases; found $caseCount"
}

Write-Output 'PASS: multilingual skill structure and safeguards are present.'
