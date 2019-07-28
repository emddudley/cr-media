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
  {%- assign distribution_links = "" -%}
  {%- for distribution in media.distributions -%}
    {%- assign service = site.data.services | where: "name",distribution.distributor | first -%}
    {%- assign media_link = service.media_link_pattern | replace: media_id_token,distribution.media_id | replace: user_id_token,distribution.user_id -%}
    {%- assign distribution_links = distribution_links | append: "[" | append: distribution.distributor | append: "](" | append: media_link | append: ")" -%}
  {%- endfor -%}
  {{ distribution_links | split: ")[" | join: "), [" }}
{% endfor %}
