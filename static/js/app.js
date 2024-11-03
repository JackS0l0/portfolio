$('.firstCarusel').slick({
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows: false,
    autoplay: true,
    speed: 10000,
    autoplaySpeed: 0,
    cssEase: 'linear',
    responsive: [
        {
            breakpoint: 1024,
            settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
            }
        },
        {
            breakpoint: 600,
            settings: {
            slidesToShow: 2,
            slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
            slidesToShow: 1,
            slidesToScroll: 1
            }
        }
    ]
});
$('.secondCarusel').slick({
    rtl: true,
    dots: false,
    infinite: true,
    speed: 300,
    slidesToShow: 4,
    slidesToScroll: 1,
    arrows: false,
    autoplay: true,
    speed: 10000,
    autoplaySpeed: 0,
    cssEase: 'linear',
    responsive: [
        {
            breakpoint: 1024,
            settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true
            }
        },
        {
            breakpoint: 600,
            settings: {
            slidesToShow: 2,
            slidesToScroll: 2
            }
        },
        {
            breakpoint: 480,
            settings: {
            slidesToShow: 1,
            slidesToScroll: 1
            }
        }
    ]
});
//Dark theme
document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("flexSwitchCheckDefault");
    const body = document.body;
    const waveImage = document.getElementById("waveImage");
    const waveImage2 = document.getElementById("waveImage2");
    const lightWaveSrc = "{% static 'media/wave1.svg' %}";
    const darkWaveSrc = "{% static 'media/wavedark1.svg' %}";
    const lightWaveSrc2 = "{% static 'media/wave2.svg' %}";
    const darkWaveSrc2 = "{% static 'media/wavedark2.svg' %}";
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        body.classList.add("dark");
        themeToggle.checked = true;
        waveImage.src = darkWaveSrc;
        waveImage2.src = darkWaveSrc2;
    } else {
        waveImage.src = lightWaveSrc;
        waveImage2.src = lightWaveSrc2;
    }
    themeToggle.addEventListener("change", () => {
        if (themeToggle.checked) {
            body.classList.add("dark");
            waveImage.src = darkWaveSrc;
            waveImage2.src = darkWaveSrc2;
            localStorage.setItem("theme", "dark");
        } else {
            body.classList.remove("dark");
            waveImage.src = lightWaveSrc;
            waveImage2.src = lightWaveSrc2;
            localStorage.setItem("theme", "light");
        }
    });
});
