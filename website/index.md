---
layout: base
title: Home
---

# Ersilia Digests

Periodic digests of literature and activity relevant to the
[Ersilia Open Source Initiative](https://ersilia.io) — AI/ML for drug discovery,
antimicrobial and antibiotic research, neglected diseases, and open science for
global health.

{% comment %} ---------- build the digest lookup + figure out the year ---------- {% endcomment %}
{% assign digests = site.pages | where_exp: "p", "p.path contains 'literature/'" | sort: "path" %}
{% assign latest = digests | last %}
{% assign year = latest.name | slice: 0, 2 | prepend: '20' %}

{% assign dkeys = "" %}
{% assign durls = "" %}
{% for d in digests %}
  {% assign stub = d.name | replace: '-literature-digest.md', '' %}
  {% assign full = stub | prepend: '20' %}
  {% assign dkeys = dkeys | append: full | append: "," %}
  {% assign durls = durls | append: d.url | append: "," %}
{% endfor %}
{% assign dkeys = dkeys | split: "," %}
{% assign durls = durls | split: "," %}

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

      <div class="cal-grid">
        {% for b in (1..jan1_dow) %}<span class="cal-cell is-blank"></span>{% endfor %}
        {% for i in (1..days) %}
          {% assign off = forloop.index0 | times: 86400 %}
          {% assign ts = base_unix | plus: off %}
          {% assign ds = ts | date: "%Y-%m-%d" %}
          {% assign nice = ts | date: "%b %-d, %Y" %}
          {% if dkeys contains ds %}
            {% assign url = "" %}
            {% for k in dkeys %}{% if k == ds %}{% assign url = durls[forloop.index0] %}{% endif %}{% endfor %}
            <a class="cal-cell has-digest" href="{{ url | relative_url }}" title="Digest — {{ nice }}" aria-label="Digest published {{ nice }}"></a>
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
    <span class="swatch empty"></span> no digest
    <span class="sep">·</span>
    <span class="swatch filled"></span> digest published — click to read
  </div>
</div>

## Recent literature digests

{% assign recent = digests | reverse %}
<ul class="card-list">
{% for d in recent limit: 8 %}
  <li>
    <a href="{{ d.url | relative_url }}">
      <span>Week of {{ d.name | replace: '-literature-digest.md', '' | prepend: '20' }}</span>
      <span class="arrow">→</span>
    </a>
  </li>
{% endfor %}
</ul>
