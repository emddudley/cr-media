---
layout: default
title: Home
---
{%- assign media_id_token = "{media_id}" -%}
{%- assign user_id_token = "{user_id}" -%}

# Critical Data

Series | Season | Episode | Title | Air Date | Links
------ | ------ | ------- | ----- | -------- | -----
{% for media in site.data.media -%}
  {{ media.series }} | {{ media.season }} | {{ media.episode }} | {{ media.title }} | {{ media.air_date }} |
  {%- assign distributions = "" -%}
  {%- for distributor in media.distributors -%}
    {%- assign service = site.data.services | where: "name",distributor.name | first -%}
    {%- assign media_link = service.media_link_pattern | replace: media_id_token,distributor.media_id -%}
    {%- assign distributions = distributions | append: "[" | append: distributor.name | append: "](" | append: media_link | append: ")" -%}
  {%- endfor -%}
  {{ distributions | split: ")[" | join: "), [" }}
{% endfor %}
