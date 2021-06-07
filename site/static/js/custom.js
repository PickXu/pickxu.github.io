function makeEmail(d, u) {
	return u + '@' + d;
}

function showEmail(sel, d, u) {
	var email = makeEmail(d, u);
	$(sel).replaceWith('<a href="mailto:' + email + '">' + email + '</a>');
}

$(document).ready(function() {
	showEmail('#ari-email', 'cs.uchicago.edu', 'arielfeldman');
	showEmail('#hao-email', 'cs.uchicago.edu', 'hajiang');
	showEmail('#michaelht-email', 'cs.uchicago.edu', 'michaelht');
	showEmail('#min-email', 'cs.uchicago.edu', 'xum');
	
});