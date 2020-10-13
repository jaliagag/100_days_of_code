const seccionesPagina = new fullpage('#fullpage', {
    autoScrolling: true
    ,fitToSection: false
    ,fitToSectionDelay: 300
    ,easing: 'easeInOutCubic' // 'ease/-in/-out
    ,scrollingSpeed: 700
    ,css3: true
    ,easingcss3: 'ease-out'
    ,loopBottom: false
    
    ,navigation: true
    ,anchors: ['inicio', 'productos', 'contacto']
    ,navigationTooltips: ['Inicio', 'Productos', 'Contacto']
    ,showActiveTooltip: false
    ,sectionsColor: ['#000', '#c2c2c2', '#000']
    ,verticalCentered: true
    ,controlArrows: true
    ,slidesNavigation: false
    ,afterLoad: function(origin, destination){
        if(destination.anchor == 'contacto'){
            document.querySelector('.footer').querySelector('h2').style.opacity = 1;
        }
    }
});