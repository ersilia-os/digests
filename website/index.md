---
layout: base
title: Home
---

# Ersilia Digests

Periodic digests of literature and activity relevant to the
[Ersilia Open Source Initiative](https://ersilia.io) — AI/ML for drug discovery,
antimicrobial and antibiotic research, neglected diseases, and open science for
global health.

Pick a week from the sidebar, or start with the most recent below.

## Recent literature digests

{% assign digests = site.pages | where_exp: "p", "p.path contains 'literature/'" | sort: "path" | reverse %}
<ul class="card-list">
{% for d in digests limit: 8 %}
  <li>
    <a href="{{ d.url | relative_url }}">
      <span>Week of {{ d.name | replace: '-literature-digest.md', '' | prepend: '20' }}</span>
      <span class="arrow">→</span>
    </a>
  </li>
{% endfor %}
</ul>
