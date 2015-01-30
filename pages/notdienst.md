title: Aktueller Notdienst

Die Notdienstzeit für die Wochenenden beginnt bereits am Freitag um 18 Uhr und endet am Montag um 9 Uhr.
An Feiertagen beginnt der Notdienst am Vortag des Feiertags um 18 Uhr und dauert bis zum Tag nach dem Feiertag um 9 Uhr.

Nachfolgend werden die Praxen, welche heute Notdienst haben angezeigt (falls heute ein Wochenende oder Feiertag ist):

<!-- Anleitung: In Klammern nach der Praxis-Überschrift eine Komma-getrennte Liste der Daten oder Datumsbereiche.
Ein Datum wird in der Form TT.MM.JJJJ angegeben und ein Datumsberiehc als TT.MM.JJJJ-TT.MM.JJJJ
Automatisch wird der Notdienst einen Tag vorher und einen Tag nachher noch angezeigt. -->


[Praxis Finkbeiner](tieraerzte/finkbeiner.html)
-----------------------------------------------------------

- 31.12.2014-01.01.2015
- 31.01.2015-01.02.2015
- 21.03.2015-22.03.2015
- 25.04.2015-26.04.2015
- 14.05.2015
- 23.05.2015-24.05.2015
- 20.06.2015-21.05.2015
- 01.08.2015-02.08.2015
- 19.09.2015-20.09.2015
- 24.10.2015-25.10.2015
- 12.12.2015
- 19.12.2015-20.12.2015)

[Mehr informationen über die Praxis](tieraerzte/finkbeiner.html)



[Praxis Leis](tieraerzte/leis.html) <small>(25.12.2014-26.12.2014, 24.01.2015-25.01.2015,14.03.2015-15.03.2015, 02.05.2015-03.05.2015, 30.05.2015-31.05.2015, 18.07.2015-19.07.2015, 22.08.2015-23.08.2015, 26.09.2015-27.09.2015, 30.10.2015-01.11.2015, 05.12.2015-06.12.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/leis.html)


[Praxis Anton](tieraerzte/anton.html) <small>(24.12.2014, 03.01.2015-04.01.2015, 21.02.2015-22.02.2015, 18.04.2015-19.04.2015, 16.05.2015-17.05.2015, 06.06.2015-07.06.2015, 25.07.2015-26.07.2015, 12.09.2015-13.09.2015, 10.10.2015-11.10.2015, 28.11.2015-29.11.2015, 26.12.2015-27.12.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/anton.html)


[Praxis Wolandowitsch](tieraerzte/wolandowitsch.html) <small>(10.01.2015-11.01.2015,07.03.2015-08.03.2015, 05.04.2015-06.04.2015, 01.05.2015, 25.05.2015, 27.06.2015-28.06.2015, 15.08.2015-16.08.2015, 03.10.2015-04.10.2015, 13.12.2015, 31.12.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/wolandowitsch.html)


[Praxis von Götz](tieraerzte/von-goetz.html) <small>(17.01.2015-18.01.2015, 09.05.2015-10.05.2015, 11.07.2015-12.07.2015 )</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/von-goetz.html)


[Praxis Bachmann](tieraerzte/bachmann.html) <small>(27.12.2014-28.12.2014, 07.02.2015-08.02.2015, 28.02.2015-01.03.2015, 28.03.2015-29.03.2015,11.04.2015-12.04.2015, 04.07.2015-05.07.2015, 08.08.2015-09.08.2015, 05.09.2015-06.09.2015, 17.10.2015-18.10.2015, 21.11.2015-22.11.2015, 24.12.2015-25.12.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/bachmann.html)


[Praxis Schmöe](tieraerzte/schmoe.html) <small>(14.02.2015-15.02.2015, 03.04.2015-04.04.2015, 13.06.2015-14.06.2015, 29.08.2015-30.08.2015, 07.11.2015-08.11.2015)</small>
-------------------------------------------------------------

[Mehr informationen über die Praxis](tieraerzte/schmoe.html)



Reguläre Dienstzeiten
===================================

Wenn oben keine Praxen eingeblendet werden, dann ist heute regulärer Dienst, und Sie können sich eine Praxis mit entsprechenden Öffnungszeiten im Menüpunkt [Praxen und Kliniken](tieraerzte.html) aussuchen.



<button id="toggle_notdienst" type="button" onclick="toggle_visibility();" class="btn btn-info btn-lg btn-block" data-toggle-text="Alle Notdienst-Tage ausblenden" autocomplete="off">Alle Notdienst-Tage einblenden</button>



<!--              ACHTUNG, AB HIER NICHT MODIFIZIEREN!

Es sei denn, Sie wissen was Sie tun :-)

Der nachfolgende JavaScript-Code wird nach dem Laden dieser Seite auf dem
Computer des Nutzers ausgeführt und zeigt den jeweils gültigen Notdienst an
und versteckt die restlichen Inhalte, wenn das Datum nicht passt.
Die Zeiträume werden in Klammern in den Überschriften der ersten beiden
Stufen angegeben (also z.B. `# Überschrift (23.04.2014, 01.05.2014)`).
Mehrere Datumsangaben werden durch Komma getrennt. Es ist auch möglich
Zeiträume anzugeben, wobei ein Bindestrich das Start- vom End-Datum
abgrenzt. Beispiel `# Überschrift (23.04.2014 - 25.04.2014)`.

(C) 2014, Samuel John (www.samueljohn.de)
Released under MIT license.
-->

<script src="moment.js"></script>
<script>

// Find html nodes on the same level after `elem`, up to but excluding the
// next element in the array `stop_tags`
function siblings_up_to (elem, stop_tags) {
    var content = [];
    do {
        content.push(elem);
        elem = elem.nextElementSibling;
    } while (elem && stop_tags.indexOf(elem.tagName) < 0);
    return content;
}

function parse_date (text) {
    return moment(text, ["DD.MM.YYYY", "DD. MMM YYYY"], "de");
}

// Return a list of pairs of moment.js objects `[ ...,[start, end],...]`
function extract_dates (text) {
    // list to hold the dates
    var dates = [];
    // regular expression to extract the text in the last pair of brackets
    var find_text_in_last_brackets_regex = /^.*\((.*)\)$/gm;
    var text_in_last_brackets = find_text_in_last_brackets_regex.exec(text);
    // console.log("regex matching: ", text_in_last_brackets);
    if (text_in_last_brackets && text_in_last_brackets.length > 1) {
        // if match, split out possible multiple dates seperated by `,`
        var date_ranges = text_in_last_brackets[1].split(',');
        // console.log("date_ranges: ", date_ranges);
        date_ranges.forEach(
            function (one_date_range_text) {
                var from_to = one_date_range_text.split('-');
                // console.log("from,to (array of string): ", from_to);
                if (from_to.length > 2) {
                    console.warn("Warning: More than two '-' found in date range.");
                    return;
                }
                // try to parse start...
                var start = parse_date(from_to[0]);
                var end = start.clone();
                if (start.isValid) {
                    // console.log("...start is valid: ", from_to[0]);
                    end.add('d', 1);  // set end to +24h later than start
                }
                // Check if there is a stop-date
                if (from_to.length > 1) {
                    // console.log("Stop-date given: ", from_to[1]);
                    end = parse_date(from_to[1]);
                    end.add('d', 1);  // so that 01.02.2014 - 02.02.2014 includes 02.02
                }
                // console.log("Parsed date from ", start, " to (+ 1d) ", end);
                dates.push([start, end]);
            }
        )
    }
    return dates;
}

function now_in_date_ranges ( date_ranges, duration_before, duration_after ) {
    var i = 0;
    for (; i < date_ranges.length; i++) {
        var date = date_ranges[i];
        if (date.length <= 0) {
            console.error("Could not extract dates for " + heading);
            return;
        }
        var start = date[0];
        var end = date[1];
        var now = moment();
        // console.log("start " + start._d);
        // console.log("now " + now._d);
        // console.log("end " + end._d);
        if (now >= start.subtract(duration_before) && now <= end.add(duration_after)) {
            console.log("☑ " + now.format('DD.MM.YYYY') + " is in date range: "
                        + date[0].subtract(duration_before).format('DD.MM.YYYY')
                        + " - "
                        + date[1].add(duration_after).format('DD.MM.YYYY'));
            return true; // don't hide this, let it stay visible
        } else {
            console.log("☐ " + now.format('DD.MM.YYYY'), " is NOT in date range: "
                        + date[0].subtract(duration_before).format('DD.MM.YYYY')
                        + " - "
                        + date[1].add(duration_after).format('DD.MM.YYYY'));
        }
    }
    return false;
}

// Search for h2 headings and hide them (with all the siblings) unless the
// current date (now) is in any of the given ranges (in brackest after the heading) or
// `before_now` long earlier than `now`.
function seek_and_hide () {
    // Not only show at beginning of first day but this long before already
    var duration_before = moment.duration(1, 'days');
    var duration_after  = moment.duration(1, 'days');
    var h2_headings = document.getElementById("content").getElementsByTagName("H2");
    console.log("seek and hide...");
    console.log("found " + h2_headings.length + " h2 headings.");
    var i = 0;
    for (; i < h2_headings.length; i++) {
        console.log("----------------- ", i );
        var heading = h2_headings[i];
        console.log("Processing " + heading.textContent);
        heading.classList.add("seek_and_hide");
        if (! now_in_date_ranges(extract_dates(heading.textContent), duration_before, duration_after)) {
            siblings_up_to(heading, ["H2", "H1"]).forEach( function (el) {
                el.display_orig = el.style.display;
                el.style.display = "none";
                el.classList.add("hidden_notdienst");
            });
        }
        console.log("done. ", i);
    }
}

function toggle_visibility() {
    console.log("toggle_visibility");
    var hidden_elements = document.getElementsByClassName("hidden_notdienst");
    console.log(hidden_elements.length + " hidden elements...");
    var i = 0;
    for (; i < hidden_elements.length; i++) {
        console.log(hidden_elements[i] + " style = " + hidden_elements[i].style.display)
        if (hidden_elements[i].style.display == "none") {
            console.log(hidden_elements[i].display_orig);
            hidden_elements[i].style.display = hidden_elements[i].display_orig;
        } else {
            hidden_elements[i].style.display = "none";
        }
    }
}

// run this shit
seek_and_hide();
</script>
