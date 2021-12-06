import { createStore } from 'vuex'

import { axios } from "@/common/api.service.js";
export default createStore({
    state: {
        UserInfo: [],
        currentGroupID: null,
        Group: [],
        GroupTasks: []
    },
    mutations: {
        setUserInfo(state, data) {
        state.UserInfo = data
        },
        setGroupName(state, data) {
            state.Group = data
        },
        setCurrentGroupID(state, data) {
            state.currentGroupID = data
        },
        setCurrentGroupTasks(state, data) {
            state.GroupTasks = data
        }
    },
    actions: {
        async getCurrentUserInfo({ state, commit }) {
            const endpoint = "/api/user/";
            try {
                const response = await axios.get(endpoint);
                commit('setUserInfo', response.data)
                commit('setCurrentGroupID', state.UserInfo.groups[0])
            } catch(error) {
                alert(error.response.statusText)
            }
        },
        async getGroupName({ commit }){
            try {
                const response = await axios.get("/api/group/");
                commit('setGroupName', response.data.results)
            } catch(error) {
                alert(error.response.statusText)
            }
        },
        async getCurrentGroupTasks({ commit, state }) {
            try {
                const response = await axios.get("/api/tasks/");
                const grouptasks = [];
                response.data.results.forEach(element => {
                    if(element.group == state.currentGroupID) {
                        grouptasks.push(element);
                    }
                });
                commit('setCurrentGroupTasks', grouptasks)
            } catch (error) {
                alert(error.response.statusText);
            }
        },
        async getCreateTask({ state }, { newTaskBody, deadline_at }){
            const endpoint = `/api/users/${state.UserInfo.id}/task/`;
            try {
                await axios.post(endpoint, {
                    taskname: newTaskBody,
                    deadline_at: deadline_at,
                    group: state.currentGroupID
                })
            }
            catch(error){
                alert(error.response.statusText);
            }
        },
        async joinCreatedGroup({state}, { joinGroupName }){
            var group_id = "";
            state.Group.forEach(group => {
                if(group.name === joinGroupName) group_id = group.id;
            });
            state.UserInfo.groups.push(group_id);
            console.error("groups: ", state.UserInfo.groups);
            const endpoint = '/api/user/';
            try {
                await axios.put(endpoint, 
                    {
                        id: state.UserInfo.id,
                        password: state.UserInfo.password,
                        username: state.UserInfo.username,
                        groups: state.UserInfo.groups
                    }
                )
            }
            catch(error){
                alert(error.response.statusText);
            }
        },
        async getCreateGroup({dispatch}, { newGroupName }){
            const endpoint = '/api/group/';
            try {
                await axios.post(endpoint, {
                     name: newGroupName
                })
                await dispatch('getGroupName');
                await dispatch('joinCreatedGroup', {joinGroupName: newGroupName});
            }
            catch(error){
                alert(error.response.statusText);
            }
        },

        async joinGroup({state}, { joinGroupID }){
            state.UserInfo.groups.push(joinGroupID);
            const endpoint = '/api/user/';
            try {
                await axios.put(endpoint, 
                    {
                        id: state.UserInfo.id,
                        password: state.UserInfo.password,
                        username: state.UserInfo.username,
                        groups: state.UserInfo.groups
                    }
                )
            }
            catch(error){
                alert(error.response.statusText);
            }
        },
        async deleteTask({state}, {task_id}) {
            const endpoint = `/api/tasks/${task_id}/`;
            try {
                await axios.delete(endpoint);
            } catch (error) {
                alert(error.response.statusText);
            }
        },
        async editTask({state}, {task_id, taskname, deadline_at}) {
            // delete a given answer from the answers array and make a delete request to the REST API
            const endpoint = `/api/tasks/${task_id}/`;
            try {
                await axios.put(endpoint, {
                    taskname: taskname,
                    deadline_at: deadline_at,
                    group: state.currentGroupID
                });
            } catch (error) {
                alert(error.response.statusText);
            }
        }
    },
    modules: {
    }
})
