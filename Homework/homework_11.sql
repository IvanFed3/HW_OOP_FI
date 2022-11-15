--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0
-- Dumped by pg_dump version 15.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actor (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.actor OWNER TO postgres;

--
-- Name: actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actor_id_seq OWNER TO postgres;

--
-- Name: actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actor_id_seq OWNED BY public.actor.id;


--
-- Name: director; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.director (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.director OWNER TO postgres;

--
-- Name: director_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.director_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.director_id_seq OWNER TO postgres;

--
-- Name: director_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.director_id_seq OWNED BY public.director.id;


--
-- Name: film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.film OWNER TO postgres;

--
-- Name: film_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.film_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.film_id_seq OWNER TO postgres;

--
-- Name: film_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.film_id_seq OWNED BY public.film.id;


--
-- Name: genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genre (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.genre OWNER TO postgres;

--
-- Name: genre_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genre_id_seq OWNER TO postgres;

--
-- Name: genre_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genre_id_seq OWNED BY public.genre.id;


--
-- Name: actor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor ALTER COLUMN id SET DEFAULT nextval('public.actor_id_seq'::regclass);


--
-- Name: director id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director ALTER COLUMN id SET DEFAULT nextval('public.director_id_seq'::regclass);


--
-- Name: film id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film ALTER COLUMN id SET DEFAULT nextval('public.film_id_seq'::regclass);


--
-- Name: genre id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre ALTER COLUMN id SET DEFAULT nextval('public.genre_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor (id, name) FROM stdin;
1	Leonardo DiCaprio
2	Denzel Washington
3	Marlon Brando
4	Morgan Freeman
5	Tom Hanks
\.


--
-- Data for Name: director; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.director (id, name) FROM stdin;
1	Steven Spielberg
2	Martin Scorsese
3	Alfred Hitchcock
4	Stanley Kubrick
5	Francis Ford Coppola
\.


--
-- Data for Name: film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.film (id, name) FROM stdin;
1	The Shawshank Redemption
2	The Godfather
3	The Dark Knight
4	The Godfather: Part II
5	The Lord of the Rings: The Return of the King
\.


--
-- Data for Name: genre; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.genre (id, name) FROM stdin;
\.


--
-- Name: actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actor_id_seq', 5, true);


--
-- Name: director_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.director_id_seq', 5, true);


--
-- Name: film_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.film_id_seq', 5, true);


--
-- Name: genre_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genre_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

