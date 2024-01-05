---
title: Schedule
layout: home
has_children: True
nav_order: 3
has_toc: False
---

# Course Schedule

{% assign weeks_list = site.html_pages | where: "layout", "week" | sort: "nav_order"  %}

|-------|--------------------|-------|--------|-----------|
| Week  | Topic / Readings   | Lab   | Studio | Homework
|:------|:-------------------|:------|:-------|:----------|
{% for node in weeks_list %} {% assign reading = site.html_pages | where: "layout",  "reading" | where: "parent", node.title | where_exp: "item", "item.visible == true or site.working == true" | first %} {% assign lab = site.html_pages | where: "layout",  "lab" | where: "parent", node.title | where_exp: "item", "item.visible == true or site.working == true"| first %} {% assign studio = site.html_pages | where: "layout", "studio" | where: "parent", node.title | where_exp: "item", "item.visible == true or site.working == true"| first %} {% assign homework = site.html_pages | where: "layout",  "homework" | where: "parent", node.title | where_exp: "item", "item.visible == true or site.working == true" | first %} | {{ node.week }} | [{{reading.topic}}]({{ reading.url | relative_url}}) | [{{lab.topic}}]({{ lab.url | relative_url}}) | [{{studio.topic}}]({{ studio.url | relative_url }}) | [{{homework.topic}}]({{ homework.url | relative_url }}) | 
{% endfor %} |-------|--------------------|-------|--------|-----------|

