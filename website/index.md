---
layout: base
title: Home
---

# Ersilia Digests

Periodic digests of literature and activity relevant to the
[Ersilia Open Source Initiative](https://ersilia.io) — AI/ML for drug discovery,
antimicrobial and antibiotic research, neglected diseases, and open science for
global health.

{% comment %} ---------- gather all digest families ---------- {% endcomment %}
{% assign litdigests = site.pages | where_exp: "p", "p.path contains 'literature/'" | sort: "path" %}
{% assign ghdigests = site.pages | where_exp: "p", "p.path contains 'github/'" | sort: "path" %}
{% assign eventdigests = site.pages | where_exp: "p", "p.path contains 'events/'" | sort: "path" %}

{% comment %} ---------- figure out the year from the most recent digest/report of any kind ---------- {% endcomment %}
{% assign alldigests = litdigests | concat: ghdigests | concat: eventdigests | sort: "name" %}
{% assign latest = alldigests | last %}
{% if latest %}
  {% assign year = latest.name | slice: 0, 2 | prepend: '20' %}
{% else %}
  {% assign year = site.time | date: "%Y" %}
{% endif %}

{% comment %} ---------- literature: date -> url lookup ---------- {% endcomment %}
{% assign litkeys = "" %}
{% assign liturls = "" %}
{% for d in litdigests %}
  {% assign full = d.name | replace: '-literature-digest.md', '' | prepend: '20' %}
  {% assign litkeys = litkeys | append: full | append: "," %}
  {% assign liturls = liturls | append: d.url | append: "," %}
{% endfor %}
{% assign litkeys = litkeys | split: "," %}
{% assign liturls = liturls | split: "," %}

{% comment %} ---------- github: date -> url lookup ---------- {% endcomment %}
{% assign ghkeys = "" %}
{% assign ghurls = "" %}
{% for d in ghdigests %}
  {% assign full = d.name | replace: '-github-digest.md', '' | prepend: '20' %}
  {% assign ghkeys = ghkeys | append: full | append: "," %}
  {% assign ghurls = ghurls | append: d.url | append: "," %}
{% endfor %}
{% assign ghkeys = ghkeys | split: "," %}
{% assign ghurls = ghurls | split: "," %}

{% comment %} ---------- events: date -> url lookup ----------
     Filename stays `-event-discovery.md` deliberately: renaming it would change the
     Pages URL and break the link in the Slack alert already published for that report.
{% endcomment %}
{% assign evkeys = "" %}
{% assign evurls = "" %}
{% for d in eventdigests %}
  {% assign full = d.name | replace: '-event-discovery.md', '' | prepend: '20' %}
  {% assign evkeys = evkeys | append: full | append: "," %}
  {% assign evurls = evurls | append: d.url | append: "," %}
{% endfor %}
{% assign evkeys = evkeys | split: "," %}
{% assign evurls = evurls | split: "," %}

{% comment %} ---------- date geometry for the grid ---------- {% endcomment %}
{% assign jan1 = year | append: '-01-01' %}
{% assign base_unix = jan1 | append: ' 12:00:00' | date: "%s" | plus: 0 %}
{% assign jan1_dow = jan1 | date: "%w" | plus: 0 %}
{% assign days = year | append: '-12-31' | date: "%j" | plus: 0 %}
{% assign ncols = jan1_dow | plus: days | minus: 1 | divided_by: 7 | plus: 1 %}
{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign today_noon = today | append: ' 12:00:00' | date: "%s" | plus: 0 %}

## {{ year }} at a glance

<div class="calendar">
  <div class="cal-scroll">
    <div class="cal-inner">

      <div class="cal-months" style="grid-template-columns: repeat({{ ncols }}, var(--cal-cell)); column-gap: var(--cal-gap);">
        {% for m in (1..12) %}
          {% capture mdate %}{{ year }}-{% if m < 10 %}0{% endif %}{{ m }}-01{% endcapture %}
          {% assign mdoy = mdate | date: "%j" | plus: 0 %}
          {% assign mcol = jan1_dow | plus: mdoy | minus: 1 | divided_by: 7 | plus: 1 %}
          <span style="grid-column: {{ mcol }};">{{ mdate | date: "%b" }}</span>
        {% endfor %}
      </div>

      {% comment %} All three families share ONE daily grid.

           A day can carry more than one digest, so cells are classified by how many
           landed that day: exactly one gets that family's colour, two or more get a
           single "multiple" colour rather than a per-combination palette — three
           families would otherwise need seven colours, which stops being readable at
           13px. A multi-digest cell can only carry one href, so it opens the first
           family present in the order literature -> github -> events, and the tooltip
           names everything published that day so nothing is hidden.
      {% endcomment %}

      <div class="cal-grid">
        {% for b in (1..jan1_dow) %}<span class="cal-cell is-blank"></span>{% endfor %}
        {% for i in (1..days) %}
          {% assign off = forloop.index0 | times: 86400 %}
          {% assign ts = base_unix | plus: off %}
          {% assign ds = ts | date: "%Y-%m-%d" %}
          {% assign nice = ts | date: "%b %-d, %Y" %}

          {% assign lu = "" %}
          {% for k in litkeys %}{% if k == ds %}{% assign lu = liturls[forloop.index0] %}{% endif %}{% endfor %}
          {% assign gu = "" %}
          {% for k in ghkeys %}{% if k == ds %}{% assign gu = ghurls[forloop.index0] %}{% endif %}{% endfor %}
          {% assign eu = "" %}
          {% for k in evkeys %}{% if k == ds %}{% assign eu = evurls[forloop.index0] %}{% endif %}{% endfor %}

          {% assign n = 0 %}
          {% assign names = "" %}
          {% assign href = "" %}
          {% if lu != "" %}
            {% assign n = n | plus: 1 %}{% assign names = "Literature" %}{% assign href = lu %}
          {% endif %}
          {% if gu != "" %}
            {% assign n = n | plus: 1 %}
            {% if names != "" %}{% assign names = names | append: " + " %}{% endif %}
            {% assign names = names | append: "GitHub" %}
            {% if href == "" %}{% assign href = gu %}{% endif %}
          {% endif %}
          {% if eu != "" %}
            {% assign n = n | plus: 1 %}
            {% if names != "" %}{% assign names = names | append: " + " %}{% endif %}
            {% assign names = names | append: "Events" %}
            {% if href == "" %}{% assign href = eu %}{% endif %}
          {% endif %}

          {% if n > 1 %}
            <a class="cal-cell has-multi" href="{{ href | relative_url }}" title="{{ names }} digests — {{ nice }} ({{ n }} published; opens the first)" aria-label="{{ names }} digests published {{ nice }}"></a>
          {% elsif lu != "" %}
            <a class="cal-cell has-lit" href="{{ lu | relative_url }}" title="Literature digest — {{ nice }}" aria-label="Literature digest published {{ nice }}"></a>
          {% elsif gu != "" %}
            <a class="cal-cell has-gh" href="{{ gu | relative_url }}" title="GitHub digest — {{ nice }}" aria-label="GitHub digest published {{ nice }}"></a>
          {% elsif eu != "" %}
            <a class="cal-cell has-ev" href="{{ eu | relative_url }}" title="Event digest — {{ nice }}" aria-label="Event digest published {{ nice }}"></a>
          {% elsif ts > today_noon %}
            <span class="cal-cell is-future" title="{{ nice }}"></span>
          {% elsif ts == today_noon %}
            <span class="cal-cell is-today" title="Today — {{ nice }}"></span>
          {% else %}
            <span class="cal-cell" title="{{ nice }}"></span>
          {% endif %}
        {% endfor %}
      </div>

    </div>
  </div>
  <div class="cal-legend">
    <span class="swatch lit"></span> literature
    <span class="sep">·</span>
    <span class="swatch gh"></span> GitHub
    <span class="sep">·</span>
    <span class="swatch ev"></span> events
    <span class="sep">·</span>
    <span class="swatch multi"></span> multiple
    <span class="sep">·</span>
    <span class="swatch empty"></span> no digest
  </div>
</div>

## Recent literature digests

{% assign recentlit = litdigests | reverse %}
<ul class="card-list">
{% for d in recentlit limit: 8 %}
  <li>
    <a href="{{ d.url | relative_url }}">
      <span>Week of {{ d.name | replace: '-literature-digest.md', '' | prepend: '20' }}</span>
      <span class="arrow">→</span>
    </a>
  </li>
{% endfor %}
</ul>

{% if ghdigests.size > 0 %}
## Recent GitHub digests

{% assign recentgh = ghdigests | reverse %}
<ul class="card-list">
{% for d in recentgh limit: 8 %}
  <li>
    <a href="{{ d.url | relative_url }}">
      <span>Week of {{ d.name | replace: '-github-digest.md', '' | prepend: '20' }}</span>
      <span class="arrow">→</span>
    </a>
  </li>
{% endfor %}
</ul>
{% endif %}

{% if eventdigests.size > 0 %}
## Recent event digests

{% assign recentevents = eventdigests | reverse %}
<ul class="card-list">
{% for d in recentevents limit: 8 %}
  <li>
    <a href="{{ d.url | relative_url }}">
      <span>{{ d.name | replace: '-event-discovery.md', '' | prepend: '20' }}</span>
      <span class="arrow">→</span>
    </a>
  </li>
{% endfor %}
</ul>
{% endif %}
