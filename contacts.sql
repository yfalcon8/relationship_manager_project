--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: events; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE events (
    id integer NOT NULL,
    user_id integer,
    scheduled_at timestamp without time zone,
    relatp_id integer,
    rcmdn text NOT NULL
);


ALTER TABLE public.events OWNER TO vagrant;

--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE events_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO vagrant;

--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE events_id_seq OWNED BY events.id;


--
-- Name: rcmdns_relatps; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE rcmdns_relatps (
    "rcmdnRelatp_id" integer NOT NULL,
    rcmdn_id integer NOT NULL,
    relatp_id integer NOT NULL
);


ALTER TABLE public.rcmdns_relatps OWNER TO vagrant;

--
-- Name: rcmdns_relatps_rcmdnRelatp_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE "rcmdns_relatps_rcmdnRelatp_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."rcmdns_relatps_rcmdnRelatp_id_seq" OWNER TO vagrant;

--
-- Name: rcmdns_relatps_rcmdnRelatp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE "rcmdns_relatps_rcmdnRelatp_id_seq" OWNED BY rcmdns_relatps."rcmdnRelatp_id";


--
-- Name: recommendations; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE recommendations (
    id integer NOT NULL,
    relatp_type character varying(3),
    rcmdn text NOT NULL
);


ALTER TABLE public.recommendations OWNER TO vagrant;

--
-- Name: recommendations_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE recommendations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recommendations_id_seq OWNER TO vagrant;

--
-- Name: recommendations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE recommendations_id_seq OWNED BY recommendations.id;


--
-- Name: relationships; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE relationships (
    id integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30),
    relatp_type character varying(3) NOT NULL,
    user_id integer,
    created_date timestamp without time zone,
    rcmdn_list text,
    email character varying(50),
    bday date,
    phone character varying(15),
    work character varying(50),
    edu character varying(50),
    fb character varying(50),
    linked_in character varying(50),
    twitter character varying(50),
    google_plus character varying(50),
    github character varying(50),
    pinterest character varying(50),
    word_press character varying(50),
    yelp character varying(50),
    skype character varying(50),
    other_social_media character varying(50),
    gift_idea text,
    goal text,
    note text,
    pet text,
    family text,
    hobby text,
    likes text,
    dislike text,
    pet_peeve text,
    fav_food text,
    fav_drink text,
    fav_restaurant text,
    sports_team text,
    fav_brand text,
    other_fav text,
    convo text,
    trait text
);


ALTER TABLE public.relationships OWNER TO vagrant;

--
-- Name: relationships_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE relationships_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.relationships_id_seq OWNER TO vagrant;

--
-- Name: relationships_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE relationships_id_seq OWNED BY relationships.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE users (
    id integer NOT NULL,
    fb_id character varying(20),
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(50) NOT NULL,
    password character varying(20) NOT NULL
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO vagrant;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE users_id_seq OWNED BY users.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY events ALTER COLUMN id SET DEFAULT nextval('events_id_seq'::regclass);


--
-- Name: rcmdnRelatp_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY rcmdns_relatps ALTER COLUMN "rcmdnRelatp_id" SET DEFAULT nextval('"rcmdns_relatps_rcmdnRelatp_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY recommendations ALTER COLUMN id SET DEFAULT nextval('recommendations_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY relationships ALTER COLUMN id SET DEFAULT nextval('relationships_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY events (id, user_id, scheduled_at, relatp_id, rcmdn) FROM stdin;
\.


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('events_id_seq', 1, false);


--
-- Data for Name: rcmdns_relatps; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY rcmdns_relatps ("rcmdnRelatp_id", rcmdn_id, relatp_id) FROM stdin;
\.


--
-- Name: rcmdns_relatps_rcmdnRelatp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('"rcmdns_relatps_rcmdnRelatp_id_seq"', 1, false);


--
-- Data for Name: recommendations; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY recommendations (id, relatp_type, rcmdn) FROM stdin;
\.


--
-- Name: recommendations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('recommendations_id_seq', 1, false);


--
-- Data for Name: relationships; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY relationships (id, first_name, last_name, relatp_type, user_id, created_date, rcmdn_list, email, bday, phone, work, edu, fb, linked_in, twitter, google_plus, github, pinterest, word_press, yelp, skype, other_social_media, gift_idea, goal, note, pet, family, hobby, likes, dislike, pet_peeve, fav_food, fav_drink, fav_restaurant, sports_team, fav_brand, other_fav, convo, trait) FROM stdin;
\.


--
-- Name: relationships_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('relationships_id_seq', 1, false);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY users (id, fb_id, first_name, last_name, email, password) FROM stdin;
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('users_id_seq', 1, false);


--
-- Name: events_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- Name: rcmdns_relatps_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY rcmdns_relatps
    ADD CONSTRAINT rcmdns_relatps_pkey PRIMARY KEY ("rcmdnRelatp_id");


--
-- Name: recommendations_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY recommendations
    ADD CONSTRAINT recommendations_pkey PRIMARY KEY (id);


--
-- Name: recommendations_rcmdn_key; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY recommendations
    ADD CONSTRAINT recommendations_rcmdn_key UNIQUE (rcmdn);


--
-- Name: relationships_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY relationships
    ADD CONSTRAINT relationships_pkey PRIMARY KEY (id);


--
-- Name: users_email_key; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users_fb_id_key; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_fb_id_key UNIQUE (fb_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: events_relatp_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY events
    ADD CONSTRAINT events_relatp_id_fkey FOREIGN KEY (relatp_id) REFERENCES relationships(id);


--
-- Name: events_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY events
    ADD CONSTRAINT events_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id);


--
-- Name: rcmdns_relatps_rcmdn_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY rcmdns_relatps
    ADD CONSTRAINT rcmdns_relatps_rcmdn_id_fkey FOREIGN KEY (rcmdn_id) REFERENCES recommendations(id);


--
-- Name: rcmdns_relatps_relatp_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY rcmdns_relatps
    ADD CONSTRAINT rcmdns_relatps_relatp_id_fkey FOREIGN KEY (relatp_id) REFERENCES relationships(id);


--
-- Name: relationships_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY relationships
    ADD CONSTRAINT relationships_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

