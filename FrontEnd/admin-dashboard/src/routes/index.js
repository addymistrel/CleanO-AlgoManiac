import { lazy } from "react";

// use lazy for better code splitting, a.k.a. load faster
const Dashboard = lazy(() => import("../pages/Dashboard"));
const Forms = lazy(() => import("../pages/Forms"));
const Cards = lazy(() => import("../pages/Cards"));
const Charts = lazy(() => import("../pages/Charts"));
const Buttons = lazy(() => import("../pages/Buttons"));
const TrackBus = lazy(() => import("../pages/TrackBus"));
const BinAdmin = lazy(() => import("../pages/BinAdmin"));
const Report = lazy(() => import("../pages/Report"));
const CamAdmin = lazy(() => import("../pages/CamAdmin"));
const CamWorker = lazy(() => import("../pages/CamWorker"));
const ManageEmployee = lazy(() => import("../pages/ManageEmployee"));
const ViewComplaints = lazy(() => import("../pages/ViewComplaints"));
const HouseDetails = lazy(() => import("../pages/HouseDetails"));
const ManageBeans = lazy(() => import("../pages/ManageBeans"));
const Modals = lazy(() => import("../pages/Modals"));
const Tables = lazy(() => import("../pages/Tables"));
const Page404 = lazy(() => import("../pages/404"));
const Blank = lazy(() => import("../pages/Blank"));

/**
 * ⚠ These are internal routes!
 * They will be rendered inside the app, using the default `containers/Layout`.
 * If you want to add a route to, let's say, a landing page, you should add
 * it to the `App`'s router, exactly like `Login`, `CreateAccount` and other pages
 * are routed.
 *
 * If you're looking for the links rendered in the SidebarContent, go to
 * `routes/sidebar.js`
 */
const routes = [
  {
    path: "/dashboard", // the url
    component: Dashboard, // view rendered
  },
  {
    path: "/forms",
    component: Forms,
  },
  {
    path: "/cards",
    component: Cards,
  },
  {
    path: "/charts",
    component: Charts,
  },
  {
    path: "/buttons",
    component: Buttons,
  },
  {
    path: "/BinAdmin",
    component: BinAdmin,
  },
  {
    path: "/ManageBeans",
    component: ManageBeans,
  },
  {
    path: "/CamAdmin",
    component: CamAdmin,
  },
  {
    path: "/CamWorker",
    component: CamWorker,
  },
  {
    path: "/TrackBus",
    component: TrackBus,
  },
  {
    path: "/Report",
    component: Report,
  },
  {
    path: "/ManageEmployee",
    component: ManageEmployee,
  },
  {
    path: "/HouseDetails",
    component: HouseDetails,
  },
  {
    path: "/ViewComplaints",
    component: ViewComplaints,
  },
  {
    path: "/modals",
    component: Modals,
  },
  {
    path: "/tables",
    component: Tables,
  },
  {
    path: "/404",
    component: Page404,
  },
  {
    path: "/blank",
    component: Blank,
  },
];

export default routes;
