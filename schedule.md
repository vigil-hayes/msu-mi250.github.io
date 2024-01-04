---
title: Schedule
layout: home
has_children: True
nav_order: 3
has_toc: False
---

# Course Schedule

<!--Zoom link: <https://msu.zoom.us/j/96651450582?pwd=SVhqOTNOMzJERW5BSVVmaEhFeWd2QT09>-->
<!-- Slack link: <https://join.slack.com/t/mi-250/signup> -->

{% assign weeks_list = site.html_pages | where: "layout", "week" | sort: "nav_order"  %}

|-------|--------------------|-------|--------|
| Week  | Topic / Readings   | Lab   | Studio |
|:------|:-------------------|:------|:-------|
{% for node in weeks_list %} {% assign reading = site.html_pages | where: "layout",  "reading" | where: "parent", node.title | where_exp: "item", "item.visible == true or site.working == true" | first %} {% assign lab = site.html_pages | where: "layout",  "lab" | where: "parent", node.title | where_exp: "item", "item.visible == true or site.working == true"| first %} {% assign studio = site.html_pages | where: "layout", "studio" | where: "parent", node.title | where_exp: "item", "item.visible == true or site.working == true"| first %} | {{ node.week }} | [{{reading.topic}}]({{ reading.url | relative_url}}) | [{{lab.topic}}]({{ lab.url | relative_url}}) | [{{studio.topic}}]({{ studio.url | relative_url }}) | 
{% endfor %} |-------|--------------------|-------|--------|

