---
layout: page
title: Service
---
#### Organizing Committee

{% assign all_service = site.data.service_auto | sort: "year" | reverse %}
<ul>
  {% assign seen_series = "" | split: "" %}
  {% for item in all_service %}
    {% if item.ENTRYTYPE == "oc" %}
      {% unless seen_series contains item.series %}
        {% assign seen_series = seen_series | push: item.series %}
        <li>{{ item.venue }} ({{ item.series }})
          {% assign years = "" | split: "" %}
          {% for oc in all_service %}
            {% if oc.ENTRYTYPE == "oc" and oc.series == item.series %}
              {% unless years contains oc.year %}
                {% assign years = years | push: oc.year | sort %}
              {% endunless %}
            {% endif %}
          {% endfor %}
          {{ years | join: ", " }}
        </li>
      {% endunless %}
    {% endif %}
  {% endfor %}
</ul>


#### Technical Program Committee and Area Chairs

<ul>
  {% assign seen_series = "" | split: "" %}
  {% for item in all_service %}
    {% if item.ENTRYTYPE == "tpc" %}
      {% unless seen_series contains item.series %}
        {% assign seen_series = seen_series | push: item.series %}
        <li>{{ item.venue }} ({{ item.series }})
          {% assign years = "" | split: "" %}
          {% for oc in all_service %}
            {% if oc.ENTRYTYPE == "tpc" and oc.series == item.series %}
              {% unless years contains oc.year %}
                {% assign years = years | push: oc.year | sort %}
              {% endunless %}
            {% endif %}
          {% endfor %}
          {{ years | join: ", " }}
        </li>
      {% endunless %}
    {% endif %}
  {% endfor %}
</ul>


#### Conference Reviewer
{% assign all_service = site.data.service_auto %}
<ul>
  {% for item in all_service %}
    {% if item.ENTRYTYPE == "reviewer" and item.keywords contains "conf" %}
        <li>{{ item.venue }} ({{ item.series }})</li>
    {% endif %}
  {% endfor %}
</ul>


#### Journal Reviewer

<ul>
  {% for item in all_service %}
    {% if item.ENTRYTYPE == "reviewer" and item.keywords contains "journal" %}
        <li>{{ item.venue }} ({{ item.series }})</li>
    {% endif %}
  {% endfor %}
</ul>

#### ACM SIGMOBILE YouTube Channel
* HotMobile'17, Mobicom'16, Mobihoc'16, Sensys'16
