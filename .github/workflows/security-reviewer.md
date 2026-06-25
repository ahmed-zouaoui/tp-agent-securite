---
on:
  pull_request:
    types: [opened, synchronize]

permissions:
  contents: read
  pull-requests: read

engine:
  id: copilot
  env:
    COPILOT_PROVIDER_BASE_URL: "https://openrouter.ai/api/v1"
    COPILOT_MODEL: "anthropic/claude-sonnet-4.6"
    COPILOT_PROVIDER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}

network:
  allowed:
    - defaults
    - openrouter.ai

tools:
  github:
    toolsets: [pull_requests, repos]

safe-outputs:
  create-pull-request-review-comment:
    max: 10
  add-labels:
    allowed: [needs-fix, security-review]
    max: 2

timeout-minutes: 10
---

# Détecter les vulnérabilités introduites par cette PR

Tu es un analyste sécurité qui relit le diff de cette pull request.

1. Récupère le diff de la PR et la liste des fichiers modifiés.
2. Pour chaque changement, cherche les vulnérabilités **introduites** :
   - injection SQL, command injection, path traversal
   - secrets ou credentials hardcodés (clés API, mots de passe)
   - désérialisation non sûre, SSRF, XSS
   - utilisation de fonctions dangereuses (`eval`, `exec`, `os.system`...)
3. Pour chaque finding, poste un commentaire **inline** sur la ligne concernée,
   en expliquant la nature du risque et une remédiation concrète.
4. Si au moins une vulnérabilité critique est trouvée, ajoute le label `needs-fix`.

Contraintes :
- Concentre-toi sur ce que la PR *introduit* ou *modifie*, pas sur la dette existante.
- Pas de faux positifs gratuits : si tu n'es pas sûr, explique le doute plutôt que d'alarmer.
- Référence toujours le fichier et le numéro de ligne.