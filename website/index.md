---
layout: base
title: Literature digests
---

## Literature digests

{% assign digests = site.pages | where_exp: "p", "p.path contains 'literature/'" | sort: "path" | reverse %}
<ul>
{% for d in digests %}
  <li><a href="{{ d.url | relative_url }}">{{ d.name | replace: '-literature-digest.md', '' | prepend: '20' }}</a></li>
{% endfor %}
</ul>
