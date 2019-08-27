---
layout: default
title: Home
---
{%- assign media_id_token = "{media_id}" -%}
{%- assign user_id_token = "{user_id}" -%}

# CR Media Directory

## Critical Role

### Campaign 1: Vox Machina

Episode | Title | Links
------- | ----- | -----
{% assign critical_role_campaign_1_episodes = site.data.media | where:"series","Critical Role" | where:"season","Campaign 1" -%}
{%- for media in critical_role_campaign_1_episodes -%}
  {{ media.episode }} | {{ media.title }} |
  {%- assign distribution_links = "" -%}
  {%- for distribution in media.distributions -%}
    {%- assign service = site.data.services | where: "name",distribution.distributor | first -%}
    {%- assign media_link = service.media_link_pattern | replace: media_id_token,distribution.media_id | replace: user_id_token,distribution.user_id -%}
    {%- assign distribution_links = distribution_links | append: "[" | append: distribution.distributor | append: "](" | append: media_link | append: ")" -%}
  {%- endfor -%}
  {{ distribution_links | split: ")[" | join: "), [" }}
{% endfor %}

### Campaign 2: Mighty Nein

Episode | Title | Links
------- | ----- | -----
{% assign critical_role_campaign_2_episodes = site.data.media | where:"series","Critical Role" | where:"season","Campaign 2" -%}
{%- for media in critical_role_campaign_2_episodes -%}
  {{ media.episode }} | {{ media.title }} |
  {%- assign distribution_links = "" -%}
  {%- for distribution in media.distributions -%}
    {%- assign service = site.data.services | where: "name",distribution.distributor | first -%}
    {%- assign media_link = service.media_link_pattern | replace: media_id_token,distribution.media_id | replace: user_id_token,distribution.user_id -%}
    {%- assign distribution_links = distribution_links | append: "[" | append: distribution.distributor | append: "](" | append: media_link | append: ")" -%}
  {%- endfor -%}
  {{ distribution_links | split: ")[" | join: "), [" }}
{% endfor %}

## Critical Role Podcast

## Social Media

### Periscope

User | Title | Links
---- | ----- | -----
{% assign social_media = site.data.media | where_exp:"item",
"item.distributions[0].distributor == 'Periscope'" -%}
{%- for media in social_media -%}
  {{ media.productions[0].producer }} | {{ media.title }} |
  {%- assign distribution_links = "" -%}
  {%- for distribution in media.distributions -%}
    {%- assign service = site.data.services | where: "name",distribution.distributor | first -%}
    {%- assign media_link = service.media_link_pattern | replace: media_id_token,distribution.media_id | replace: user_id_token,distribution.user_id -%}
    {%- assign distribution_links = distribution_links | append: "[" | append: distribution.distributor | append: "](" | append: media_link | append: ")" -%}
  {%- endfor -%}
  {{ distribution_links | split: ")[" | join: "), [" }}
{% endfor %}

### Twitter

User | Title | Links
---- | ----- | -----
{% assign social_media = site.data.media | where_exp:"item",
"item.distributions[0].distributor == 'Twitter'" -%}
{%- for media in social_media -%}
  {{ media.productions[0].producer }} | {{ media.title }} |
  {%- assign distribution_links = "" -%}
  {%- for distribution in media.distributions -%}
    {%- assign service = site.data.services | where: "name",distribution.distributor | first -%}
    {%- assign media_link = service.media_link_pattern | replace: media_id_token,distribution.media_id | replace: user_id_token,distribution.user_id -%}
    {%- assign distribution_links = distribution_links | append: "[" | append: distribution.distributor | append: "](" | append: media_link | append: ")" -%}
  {%- endfor -%}
  {{ distribution_links | split: ")[" | join: "), [" }}
{% endfor %}

## Guest Appearances
